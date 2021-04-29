from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Lesson, Course


def get_lessons_list(self):
    return get_list_or_404(Lesson.objects.select_related('course'),
                           course__pk=self.kwargs['courses_pk'])


def get_lesson_detail(self):
    return get_object_or_404(Lesson.objects.select_related('course'),
                             course__pk=self.kwargs['courses_pk'],
                             pk=self.kwargs['pk'])


def get_courses_list(self):
    return get_list_or_404(Course)


def get_course_detail(self, pk):
    return get_object_or_404(Course, pk=pk)