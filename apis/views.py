from django.shortcuts import render


from rest_framework import generics

from quiz.models import *
from .serializers import *


class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class OptionList(generics.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = QuestionSerializer


class OptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Options.objects.all()
    serializer_class = QuestionSerializer