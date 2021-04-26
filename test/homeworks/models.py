from django.db import models
from django.conf import settings

from courses.models import Lesson


class HomeworkFile(models.Model):
    file = models.FileField()

    def __str__(self):
        return f'homework file {self.id}'


class HomeworkAnswerFile(models.Model):
    file = models.FileField()

    def __str__(self):
        return f'homework answer file {self.id}'


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson)
    title = models.CharField(max_length=100)
    description = models.TextField()
    additional_files = models.ForeignKey(HomeworkFile)

    def __str__(self):
        return self.title


class HomeworkAnswer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    homework = models.ForeignKey(Homework)
    homework_answer_file = models.ForeignKey(HomeworkAnswerFile)

    def __str__(self):
        return f'homework {self.homework.id} user {self.user.id}'


class HomeworkReview(models.Model):
    score = models.IntegerField()
    review_text = models.TextField()
    homework_answer = models.HomeworkAnswer(HomeworkAnswer)

    def __str__(self):
        return f'homework answer {self.homework_answer.id} score {self.score}'
