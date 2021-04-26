from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Lesson


def get_lessons_list(self):
    return get_list_or_404(Lesson, course__pk=self.kwargs['pk'])


def get_lesson_detail(self):
    return get_object_or_404(Lesson,
                             course__pk=self.kwargs['pk'],
                             id=self.kwargs['lesson_pk'])
