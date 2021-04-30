from django.urls import path, include
from rest_framework_nested import routers

from .viewsets import HomeworkViewSet, HomeworkAnswerViewSet, HomeworkReviewViewSet
from courses.api.viewsets import CourseViewSet, LessonViewSet

router = routers.SimpleRouter()
router.register('courses', CourseViewSet)

lesson_router = routers.NestedSimpleRouter(router, 'courses', lookup='courses')
lesson_router.register('lessons', LessonViewSet, basename='course-lessons')

homework_router = routers.NestedSimpleRouter(lesson_router,
                                             'lessons',
                                             lookup='lessons')
homework_router.register('homeworks',
                         HomeworkViewSet,
                         basename='lessons-homeworks')

homework_answer_router = routers.NestedSimpleRouter(homework_router,
                                                    'homeworks',
                                                    lookup='homeworks')
homework_answer_router.register('homework_answers',
                                HomeworkAnswerViewSet,
                                basename='homeworks-homework_answers')

homework_review_router = routers.NestedSimpleRouter(homework_answer_router,
                                                    'homework_answers',
                                                    lookup='homework_answers')
homework_review_router.register('homework_reviews',
                                HomeworkReviewViewSet,
                                basename='homeworks_answers-homework_reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(lesson_router.urls)),
    path('', include(homework_router.urls)),
    path('', include(homework_answer_router.urls)),
    path('', include(homework_review_router.urls)),
]
