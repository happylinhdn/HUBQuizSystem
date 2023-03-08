from django.db import models
from django.conf import settings

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=800,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self): 
        if len(self.question) > 25:
            return self.question[0:25]
        else:
            return self.question

class ExamModel(models.Model):
    ma_de = models.CharField(max_length=50)
    questions = models.ManyToManyField(QuesModel)
    duration = models.IntegerField(default=120)

    def __str__(self):
        return str(self.ma_de)
class AssignmentSeason(models.Model):
    name = models.CharField(max_length=50) # Tên kỳ thi
    def __str__(self):
        return str(self.name)

class AssignmentModel(models.Model):
    assignment_season = models.ForeignKey(AssignmentSeason, on_delete=models.CASCADE, related_name='assignment_season', null=True, blank=True)
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE, related_name='exams') #De Thi
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    time_start = models.TimeField()
    time_end = models.TimeField()
    status = models.CharField(max_length=10, default='Assigned', null=True, blank=True) # todo: let check what is status field ?
    answers = models.TextField(null=True, blank=True) # should as TextField json format [{'id':question.id, 'choice':'A,B,C,D'}]
    wrong = models.IntegerField(default=-1, null=True, blank=True)
    correct = models.IntegerField(default=-1, null=True, blank=True)

    def __str__(self):
        return str(self.user.username + '_' + self.exam.ma_de)

class QuesSample(models.Model):
    question = models.CharField(max_length=800,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

class QuizMatrix(models.Model):
    name_of_matrix = models.CharField(max_length=200) #Ten ma tran -> Cau 1, de mau ABC
    question_samples = models.ManyToManyField(QuesSample, blank=True) # danh sach cau hoi cua ma tran
    file = models.FileField(upload_to="matrix", null=True, blank=True) # support tao matrix tu file
    def __str__(self):
        return str(self.name_of_matrix)

class QuizSample(models.Model):
    name_of_sample = models.CharField(max_length=200) #Ten de mau -> De mau ABC, nam 2023
    quiz_matrixs = models.ManyToManyField(QuizMatrix, blank=True) # Danh sach ma tran de
    def __str__(self):
        return str(self.name_of_sample) + ' - ' + str(len(self.quiz_matrixs.all()) or 0) + ' Câu hỏi'