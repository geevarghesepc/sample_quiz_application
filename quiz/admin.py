from django.contrib import admin
from . models import Quiz, Question, Options, UserQuizDetails, UserQuiz
# Register your models here.


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(UserQuizDetails)
admin.site.register(UserQuiz)