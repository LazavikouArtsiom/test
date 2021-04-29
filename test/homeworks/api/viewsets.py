from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from homeworks.models import (Homework, HomeworkAnswer, HomeworkReview)
from .serializers import (HomeworkSerializer, HomeworkAnswerSerializer,
                          HomeworkReviewSerializer)
from utils.permissions import IsSubscribed, IsSubscribedOrIsAdmin
from homeworks.utils.permissions import IsHomeworkAnswerOwner
from homeworks.selectors import (
    get_homework_answers_list,
    get_homework_answers_detail,
    get_homework_review_detail,
    get_homeworks_list,
    
)


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]

    def get_queryset(self):
        return get_homeworks_list(self, request)


class HomeworkAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkAnswerSerializer
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]

    def get_queryset(self):
        if IsAdminUser():
            return get_homework_answers_list(self, request)
        elif IsHomeworkAnswerOwner():
            return get_homework_answers_detail(self, request)


class HomeworkReviewViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkReviewSerializer
    permission_classes = [IsAdminUser, IsHomeworkAnswerOwner]

    def get_queryset(self):
        return get_homework_review_detail(self)