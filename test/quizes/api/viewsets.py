from rest_framework import viewsets
from quizes.models import Quiz
from .serializers import QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

