from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import QuestionSerializer
from quizes.models import Question


class QuestionsListCreateAPIView(ListCreateAPIView):

    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.first()