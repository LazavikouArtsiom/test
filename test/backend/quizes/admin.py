from django.contrib import admin
from .models import (Quiz, Question, AnswerOption,
                     UserQuiz, UserQuizQuestionAnswer)

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(AnswerOption)
admin.site.register(UserQuiz)
admin.site.register(UserQuizQuestionAnswer)
