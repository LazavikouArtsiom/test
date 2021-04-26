from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from courses.models import Lesson, Course
from courses.selectors import get_lesson_detail, get_lessons_list

from .serializers import LessonSerializer


class LessonListCreateAPIView(ListCreateAPIView):

    serializer_class = LessonSerializer

    def get_queryset(self):
        return get_lessons_list(self)


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = LessonSerializer
    
    def get_queryset(self):
        return get_lesson_detail(self)