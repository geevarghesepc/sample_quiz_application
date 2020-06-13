from django.urls import path

from .views import *

urlpatterns = [
    path('quizzes', QuizList.as_view()),
    path('quizzes/<int:pk>', QuizDetail.as_view()),
    path('questions', QuestionList.as_view()),
]