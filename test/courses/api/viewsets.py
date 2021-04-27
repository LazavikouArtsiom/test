from rest_framework import viewsets
from rest_framework.decorators import action

from courses.models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    @action(detail=True, methods=['post'], permission_classes=[], name='subscribe')
    def subscribe(self, request, pk=None):
        user = self.request.user
        course = Course.objects.get(pk=pk)
        user.courses.add(course)
        user.save()
        return Responce({'status': 'subscription added'})

    @action(detail=True, methods=['post'], permission_classes=[], name='unsubscribe')
    def unsubscribe(self, request, pk=None):
        user = self.request.user
        course = Course.objects.get(pk=pk)
        user.courses.remove(course)
        user.save()
        return Responce({'status': 'subscription deleted'})


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
