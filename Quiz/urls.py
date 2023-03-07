from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='quiz-home'),
    path('quiz-addQuestion/', addQuestion, name='quiz-addQuestion'),
    path('quiz-login/', loginPage, name='quiz-login'),
    path('quiz-logout/', logoutPage, name='quiz-logout'),
    path('quiz-register/', registerPage, name='quiz-register'),
]