from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from quizes.models import Quiz, Question, AnswerOption
from .serializers import QuizSerializer, QuestionSerializer, AnswerOptionSerializer
from utils.permissions import IsSubscribed, IsSubscribedOrIsAdmin


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]


class AnswerOptionViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerOptionSerializer
    queryset = AnswerOption.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]
