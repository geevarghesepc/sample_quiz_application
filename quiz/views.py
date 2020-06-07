from django.shortcuts import render
from django.views import generic
from quiz_project import config
# Create your views here.
from . models import *


class HomeView(generic.ListView):
    def get(self, *args, **kwargs):
        context = {"menus": config.menus}
        return render(self.request, 'home.html', context)


class QuizList(generic.ListView):

    def get(self, *args, **kwargs):
        context = {"menus": config.menus}
        quizes = Quiz.objects.all()
        context['quizes'] = quizes
        return render(self.request, 'quiz_list.html', context)


class StartQuiz(generic.ListView):
    def get(self, request, *args, **kwargs):
        quiz_id = request.GET.get("id", None)
        context = {"menus": config.menus}
        quiz = Quiz.objects.get(pk=quiz_id)
        questions = Question.objects.select_related('option_a').filter(quiz_id=quiz_id).values()
        context['quiz'] = quiz
        context['questions'] = questions
        return render(self.request, 'start_quiz.html', context)
