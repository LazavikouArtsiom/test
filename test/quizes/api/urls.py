from django.urls import path, include
from rest_framework import routers

from .viewsets import QuizViewSet

router = routers.SimpleRouter()
router.register(r'quizes', QuizViewSet)

from .views import QuestionsListCreateAPIView, QuestionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<int:course_id>/quizes/<int:pk>/questions/', QuestionsListCreateAPIView.as_view()),
    path('<int:course_id>/quizes/<int:pk>/questions/<int:question_id>/', QuestionRetrieveUpdateDestroyAPIView.as_view())
#     path('quizes/<int:pk>/questions/<int:question_id/answer_options/', answerOptions list
] + router.urls

