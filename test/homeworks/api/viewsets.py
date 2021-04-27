from rest_framework import viewsets
from homeworks.models import Homework
from .serializers import HomeworkSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()