from rest_framework import serializers
from quiz.models import *


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all(), many=True)

    class Meta:
        model = Question
        fields = '__all__'


class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = '__all__'
