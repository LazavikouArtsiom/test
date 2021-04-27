from rest_framework import viewsets
from quizes.models import Quiz, Question, AnswerOption
from .serializers import QuizSerializer, QuestionSerializer, AnswerOptionSerializer


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerOptionViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerOptionSerializer
    queryset = AnswerOption.objects.all()
