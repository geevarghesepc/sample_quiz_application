from django.shortcuts import render


from rest_framework import generics

from quiz.models import *
from .serializers import QuizSerializer


class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer