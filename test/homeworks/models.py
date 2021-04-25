from django.db import models
from courses.models import Lesson

class Homework(models.Model):
    lesson = models.ForeignKey(Lesson)


class HomeworkAnswer(models.Model):
    # user
    homework = models.ForeignKey(Homework)


class HomeworkReview(models.Model):
    homework_answer = models.HomeworkAnswer(HomeworkAnswer)
