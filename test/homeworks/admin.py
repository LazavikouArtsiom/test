from django.contrib import admin
from .models import (Homework, HomeworkAnswer, HomeworkAnswerFile,
                    HomeworkFile, HomeworkReview)

admin.site.register(Homework)
admin.site.register(HomeworkAnswer)
admin.site.register(HomeworkAnswerFile)
admin.site.register(HomeworkFile)
admin.site.register(HomeworkReview)
