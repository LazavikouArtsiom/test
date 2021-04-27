from django.urls import path, include
from rest_framework_nested import routers

from .viewsets import HomeworkViewSet
from courses.api.viewsets import CourseViewSet, LessonViewSet

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)

lesson_router = routers.NestedSimpleRouter(router, r'courses', lookup='courses')
lesson_router.register(r'lessons', LessonViewSet, basename='course-lessons')

homework_router = routers.NestedSimpleRouter(lesson_router, r'lessons', lookup='lessons')
homework_router.register(r'homeworks', HomeworkViewSet, basename='lessons-homeworks')

urlpatterns = [
     path('', include(router.urls)),
     path('', include(lesson_router.urls)),
     path('', include(homework_router.urls)),
]
