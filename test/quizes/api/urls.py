from django.urls import path, include
from rest_framework import routers

from .viewsets import QuizViewSet

router = routers.SimpleRouter()
router.register(r'quizes', QuizViewSet)

# from .views import LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

urlpatterns = [
#     path('', Quizes list,
#     path('<int:pk>/', Quiz detail
#     path('<int:pk>/questions/', questions list
#     path('<int:pk>/questions/<int:question_id>', question detail
#     path('<int:pk>/questions/<int:question_id/answer_options/', answerOptions list
] + router.urls

print(router.urls)
