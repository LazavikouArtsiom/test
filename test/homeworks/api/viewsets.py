from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from homeworks.models import Homework, HomeworkAnswer, HomeworkReview
from .serializers import HomeworkSerializer, HomeworkAnswerSerializer, HomeworkReviewSerializer
from utils.permissions import IsSubscribed, IsSubscribedOrIsAdmin


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]


class HomeworkAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkAnswerSerializer
    queryset = HomeworkAnswer.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribed]


class HomeworkReviewViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkReviewSerializer
    queryset = HomeworkReview.objects.all()
    permission_classes = [IsAdminUser]
