from django.urls import path
from .views import *

urlpatterns = [
    path('', quizHome, name='quiz-home'),
    path('do-assignment/<int:pk>', doAssignment, name='do-assignment'),
    path('quiz-addQuestion', addQuestion, name='quiz-addQuestion'),
    path('quiz-login/', loginPage, name='quiz-login'),
    path('quiz-logout/', logoutPage, name='quiz-logout'),
    path('quiz-register/', registerPage, name='quiz-register'),
    path('quiz-assignment-season-list', AssignmentSeasonListView.as_view(), name='quiz-assignment-season-list'),
    path('quiz-assignment-season-detail/<int:pk>', assignmentSeasonDetailView, name='quiz-assignment-season-detail'),
    path('quiz-sample-list', QuizSampleListView.as_view(), name='quiz-sample-list'),
    path('add-ques-matrix', addQuesMatrix, name='add-question-matrix'),
]