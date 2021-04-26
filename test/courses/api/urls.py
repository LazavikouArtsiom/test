from django.urls import path, include
from rest_framework import routers

from .viewsets import CourseViewSet
from .views import LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('courses/<int:pk>/lessons/', LessonListCreateAPIView.as_view()),
    path('courses/<int:pk>/lessons/<int:lesson_pk>/',
         LessonRetrieveUpdateDestroyAPIView.as_view()),
] + router.urls

