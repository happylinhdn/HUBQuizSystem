from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.defaults import bad_request
from django.core.exceptions import BadRequest



# Create your views here.
def quizHome(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context = {
                'user':request.user
            }
            return render(request,'Quiz/teacher/teacher-home.html',context)
        else:
            assignments = AssignmentModel.objects.filter(user = request.user)
            context = {
                'user':request.user,
                'assigment':assignments
            }
            return render(request,'Quiz/home.html',context)
    else:
        return render(request,'Quiz/home-empty-user.html')

@login_required
def doAssignment(request, pk):
    if request.method == 'POST':
        assignment = AssignmentModel.objects.filter(id=pk)
        if assignment and len(assignment) > 0:
            questions = assignment[0].exam.questions.all()
            score = 0
            wrong = 0
            correct = 0
            total = 0
            student_ans = request.POST
            
            for q in questions:
                total+=1
                if q.ans == student_ans.get(str(q.id)):
                    score += 10
                    correct += 1
                else:
                    wrong+=1
            percent = score/(total*10) *100
            
            context = {
                'score':score,
                'time': request.POST.get('timer'),
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
            }

            assignment[0].status = 'Submitted'
            assignment[0].wrong = wrong
            assignment[0].correct = correct
            assignment[0].answers = student_ans.dict()
            assignment[0].save()
            
            return render(request, 'Quiz/result.html', context)
        else:
            return bad_request(request, BadRequest("Invalid request; see documentation for correct paramaters"))
    else:
        assignments = AssignmentModel.objects.filter(id=pk)
        questions = None
        if assignments and len(assignments) > 0:
            assignment = assignments[0]
            questions = assignment.exam.questions.all()
            if assignment.status == 'Submitted':
                wrong = assignment.wrong
                correct = assignment.correct
                score = correct * 10 
                total = len(questions)
                percent = score/(total*10) *100
                context = {
                    'score':score,
                    'time': 120,
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request, 'Quiz/result.html', context)
            

        context = {
            'questions':questions
        }
        return render(request,'Quiz/do-quiz.html',context)

@login_required
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('quiz-home') 
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('quiz-home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')

#Teacher views
from django.views.generic import ListView, DetailView
class AssignmentSeasonListView(ListView):
    queryset = AssignmentSeason.objects.all()#.order_by('-date')
    template_name = 'Quiz/teacher/teacher-assignment-season-list.html'
    context_object_name = 'Seasons'
    paginate_by = 8

@login_required
def assignmentSeasonDetailView(request, pk):
    season = get_object_or_404(AssignmentSeason, pk=pk)
    assignments = AssignmentModel.objects.filter(assignment_season=season)
    context = {
        "Season": season,
        "assignments": assignments
    }
    return render(request, "Quiz/teacher/teacher-assignment-season-detail.html", context)

class QuizSampleListView(ListView):
    queryset = QuizSample.objects.all()#.order_by('-date')
    template_name = 'Quiz/teacher/teacher-quiz-sample-list.html'
    context_object_name = 'QuizSamples'
    paginate_by = 8