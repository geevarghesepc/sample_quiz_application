from django.urls import path
from .views import *
app_name = 'quiz'

urlpatterns = [
    path('take_quiz', QuizList.as_view(), name='take_quiz'),
    path('start_quiz', StartQuiz.as_view(), name='start_quiz')
]