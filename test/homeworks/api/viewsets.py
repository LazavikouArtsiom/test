from rest_framework import viewsets
from homeworks.models import Homework, HomeworkAnswer, HomeworkReview
from .serializers import HomeworkSerializer, HomeworkAnswerSerializer, HomeworkReviewSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()


class HomeworkAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkAnswerSerializer
    queryset = HomeworkAnswer.objects.all()


class HomeworkReviewViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkReviewSerializer
    queryset = HomeworkReview.objects.all()