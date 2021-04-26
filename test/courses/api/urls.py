from django.urls import path, include
from rest_framework import routers

from .viewsets import CourseViewSet, LessonViewSet
from .views import LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)

lesson_router = routers.SimpleRouter()
lesson_router.register(r'courses/<int:id>/lessons', LessonViewSet)

urlpatterns = [
    # path('courses/<int:pk>/lessons/', LessonListCreateAPIView.as_view()),
    # path('courses/<int:pk>/lessons/<int:lesson_pk>/',
    #      LessonRetrieveUpdateDestroyAPIView.as_view()),
] + router.urls + lesson_router.urls
print(router.urls)

