from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from utils.permissions import IsSubscribed, IsSubscribedOrIsAdmin
from courses.models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from courses.selectors import (
                                get_lessons_list,
                                get_lesson_detail,
                                get_courses_list,
                                get_course_detail,
                               )


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = get_courses_list(self)

    @action(detail=True,
            methods=['post'],
            permission_classes=[IsAuthenticated],
            name='subscribe')
    def subscribe(self, request, pk=None):
        user = self.request.user
        course = get_course_detail(self, pk)
        user.courses.add(course)
        user.save()
        return Response({'status': 'subscription added'})


    @action(detail=True,
            methods=['post'],
            permission_classes=[IsAuthenticated, IsSubscribed],
            name='unsubscribe')
    def unsubscribe(self, *args, **kwargs):
        user = self.request.user
        course = get_course_detail(self, pk=self.kwargs['pk'])
        user.courses.remove(course)
        user.save()
        return Response({'status': 'subscription deleted'})


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]

    def get_queryset(self):
        if self.action in ('retrieve', 'update', 'destroy', 'partial_update'):
            return get_lesson_detail(self)
        return get_lessons_list(self)
