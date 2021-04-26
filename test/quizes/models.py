from django.db import models
from django.conf import settings

from courses.models import Course


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.title


class Question(models.Model):
    description = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz)
    _has_right = models.BooleanField()
    is_multianswered = models.BooleanField()
    points_price = model.IntegerField()

    def __str__(self):
        return self.description


class AnswerOption(models.Model):
    description = models.CharField(max_length=255)
    question = models.ForeignKey(Question)
    is_right = models.BooleanField()

    def __str__(self):
        return self.description


class UserQuiz(models.Model):
    result = models.IntegerField()
    quiz = models.ForeignKey(Quiz)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'user {self.user.id} quiz {self.quiz.title} result {self.result}'


class UserQuizQuestionAnswer(models.Model):
    pass
