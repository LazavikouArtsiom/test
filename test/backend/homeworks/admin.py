from django.contrib import admin
from .models import (Homework, HomeworkAnswer, HomeworkReview)

admin.site.register(Homework)
admin.site.register(HomeworkAnswer)
admin.site.register(HomeworkReview)
