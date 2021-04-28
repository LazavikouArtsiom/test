from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from utils.permissions import IsSubscribed, IsSubscribedOrIsAdmin
from courses.models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    @action(detail=True,
            methods=['post'],
            permission_classes=[IsAuthenticated],
            name='subscribe')
    def subscribe(self, request, pk=None):
        user = self.request.user
        course = Course.objects.get(pk=pk)
        user.courses.add(course)
        user.save()
        return Response({'status': 'subscription added'})

    @action(detail=True,
            methods=['post'],
            permission_classes=[IsAuthenticated, IsSubscribed],
            name='unsubscribe')
    def unsubscribe(self, *args, **kwargs):
        user = self.request.user
        course = Course.objects.get(pk=self.kwargs['pk'])
        user.courses.remove(course)
        user.save()
        return Response({'status': 'subscription deleted'})


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]
    
