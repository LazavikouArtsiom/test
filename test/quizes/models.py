from django.db import models
from courses.models import Course

class Quiz(models.Model):
    course = models.ManyToManyField(Course)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)


class AnswerOption(models.Model):
    question = models.ForeignKey(Question)


class UserQuiz(models.Model):
    result = models.IntegerField()
    quiz = models.ForeignKey(Quiz)
    # user


class UserQuizQuestionAnswer(models.Model):
    pass
