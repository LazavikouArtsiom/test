from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from homeworks.models import (Homework, HomeworkAnswer, HomeworkReview)
from .serializers import (HomeworkSerializer, HomeworkAnswerSerializer,
                          HomeworkReviewSerializer)
from utils.permissions import IsSubscribed, IsSubscribedOrIsAdmin
from homeworks.utils.permissions import IsHomeworkAnswerOwner


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]


class HomeworkAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkAnswerSerializer
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]

    def get_queryset(self):
        homework_id = self.request.parser_context['kwargs'].get('homeworks_pk')
        if IsAdminUser():
            return HomeworkAnswer.objects.filter(homework_id=homework_id)
        elif IsHomeworkAnswerOwner():
            return HomeworkAnswer.objects.filter(user=request.user).filter(
                homework_id=homework_id)


class HomeworkReviewViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkReviewSerializer
    permission_classes = [IsAdminUser, IsHomeworkAnswerOwner]

    def get_queryset(self):
        homework_answer_id = self.request.parser_context['kwargs'].get(
            'homework_answers_pk')
        return HomeworkReview.objects.filter(
            homework_answer_id=homework_answer_id)