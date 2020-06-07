# Generated by Django 3.0.7 on 2020-06-07 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_quiz',
            },
        ),
        migrations.AddField(
            model_name='options',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='UserQuizDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='quiz.Options')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
                ('user_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='quiz.Options')),
                ('user_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.UserQuiz')),
            ],
            options={
                'db_table': 'user_quiz_details',
            },
        ),
        migrations.AddField(
            model_name='userquiz',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
        ),
        migrations.AddField(
            model_name='userquiz',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
