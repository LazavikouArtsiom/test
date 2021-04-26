from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from courses.models import Course


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    course = models.ManyToManyField(Course)
    is_daily = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'quizes'
        unique_together = ['title', 'course']

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    _has_right = models.BooleanField()
    is_multianswered = models.BooleanField(default=False)
    points_price = models.IntegerField()

    class Meta:
        unique_together = ['title', 'description']

    def __str__(self):
        return self.description


class AnswerOption(models.Model):
    description = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_right = models.BooleanField()

    class Meta:
        unique_together = ['description', 'question']

    def __str__(self):
        return self.description


class UserQuiz(models.Model):
    result = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)],
        blank=True,
        null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ['quiz', 'user']

    def __str__(self):
        return f'user {self.user.id} quiz {self.quiz.title} result {self.result}'


class UserQuizQuestionAnswer(models.Model):
    user_quiz = models.ForeignKey(UserQuiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user_quiz', 'question', 'answer']
