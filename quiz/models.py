from django.db import models
from user.models import User


class Quiz(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'quiz'

    def __str__(self):
        return self.name


class Options(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'options'

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    option_a = models.ForeignKey(Options, on_delete=models.DO_NOTHING, related_name='option_a')
    option_b = models.ForeignKey(Options, on_delete=models.DO_NOTHING, related_name='option_b')
    option_c = models.ForeignKey(Options, on_delete=models.DO_NOTHING, related_name='option_c')
    option_d = models.ForeignKey(Options, on_delete=models.DO_NOTHING, related_name='option_d')

    # option_a = models.CharField(max_length=100)
    # option_b = models.CharField(max_length=100)
    # option_c = models.CharField(max_length=100)
    # option_d = models.CharField(max_length=100)
    answer = models.ForeignKey(Options, on_delete=models.DO_NOTHING)
    score = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'question'

    def __str__(self):
        return self.question


class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_quiz'


class UserQuizDetails(models.Model):
    user_quiz = models.ForeignKey(UserQuiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.ForeignKey(Options, on_delete=models.CASCADE, related_name='user_answer')
    correct_answer = models.ForeignKey(Options, on_delete=models.CASCADE, related_name='correct_answer')

    class Meta:
        db_table = 'user_quiz_details'
