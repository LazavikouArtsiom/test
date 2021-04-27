from django.contrib import admin
from .models import (Homework, HomeworkAnswer, HomeworkFile, HomeworkReview)

admin.site.register(Homework)
admin.site.register(HomeworkAnswer)
admin.site.register(HomeworkFile)
admin.site.register(HomeworkReview)
