from django.urls import path, include
from rest_framework_nested import routers

from .viewsets import QuizViewSet, QuestionViewSet, AnswerOptionViewSet
from courses.api.viewsets import CourseViewSet

course_router = routers.SimpleRouter()
course_router.register(r'courses', CourseViewSet)

router = routers.NestedSimpleRouter(course_router, r'courses', lookup='courses')
router.register(r'quizes', QuizViewSet, basename='courses-quizes')

question_router = routers.NestedSimpleRouter(router, r'quizes', lookup='quizes')
question_router.register(r'questions', QuestionViewSet, basename='quizes-questions')

answer_option_router = routers.NestedSimpleRouter(question_router, r'questions', lookup='questions')
answer_option_router.register(r'answer_options', AnswerOptionViewSet, basename='questions-answeroptions')

urlpatterns = [
     path('', include(router.urls)),
     path('', include(question_router.urls)),
     path('', include(answer_option_router.urls)),
]
