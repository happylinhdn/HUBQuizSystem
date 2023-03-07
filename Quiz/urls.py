from django.urls import path
from .views import *

urlpatterns = [
    path('', quizHome, name='quiz-home'),
    path('do-assignment/<int:pk>', doAssignment, name='do-assignment'),
    path('quiz-addQuestion', addQuestion, name='quiz-addQuestion'),
    path('quiz-login/', loginPage, name='quiz-login'),
    path('quiz-logout/', logoutPage, name='quiz-logout'),
    path('quiz-register/', registerPage, name='quiz-register'),
]