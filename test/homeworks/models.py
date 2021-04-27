from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from courses.models import Lesson


class HomeworkFile(models.Model):
    homework_file = models.FileField(upload_to=r'test\media\files',
                                     unique=True)

    def __str__(self):
        return f'homework file {self.id}'


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    additional_files = models.ManyToManyField(HomeworkFile, )

    class Meta:
        unique_together = [
            'title',
            'description',
            'lesson',
        ]

    def __str__(self):
        return self.title


class HomeworkAnswer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    homework = models.ForeignKey(Homework,
                                 on_delete=models.SET_NULL,
                                 null=True)
    text = models.TextField()

    class Meta:
        unique_together = ['user', 'homework']

    def __str__(self):
        return f'homework {self.homework.id} user {self.user.id}'


class HomeworkReview(models.Model):
    score = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1),
                               MaxValueValidator(5)])
    review_text = models.TextField(unique=True)
    homework_answer = models.ForeignKey(HomeworkAnswer,
                                        on_delete=models.CASCADE)

    def __str__(self):
        return f'homework answer {self.homework_answer.id} score {self.score}'
