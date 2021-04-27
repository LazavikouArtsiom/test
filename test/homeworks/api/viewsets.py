from rest_framework import viewsets
from homeworks.models import Homework, HomeworkAnswer
from .serializers import HomeworkSerializer, HomeworkAnswerSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()


class HomeworkAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkAnswerSerializer
    queryset = HomeworkAnswer.objects.all()
