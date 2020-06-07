from django.urls import path

from .views import QuizList

urlpatterns = [
    path('quizzes', QuizList.as_view()),
]