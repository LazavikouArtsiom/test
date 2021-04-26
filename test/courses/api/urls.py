from django.urls import path, include
from django.conf.urls import url
from rest_framework_nested import routers

from .viewsets import CourseViewSet, LessonViewSet
from .views import LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)

lesson_router = routers.NestedSimpleRouter(router, r'courses', lookup='courses')
lesson_router.register(r'lessons', LessonViewSet, basename='course-lessons')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(lesson_router.urls)),
]

