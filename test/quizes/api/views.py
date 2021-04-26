from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import QuestionSerializer, AnswerOptionSerializer
from quizes.models import Question, AnswerOption


class QuestionsListCreateAPIView(ListCreateAPIView):

    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.first()


class AnswerOptionsListCreateAPIView(ListCreateAPIView):

    serializer_class = AnswerOptionSerializer

    def get_queryset(self):
        return AnswerOption.objects.first()