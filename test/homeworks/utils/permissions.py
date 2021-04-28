from rest_framework.permissions import BasePermission, IsAdminUser

from courses.models import Course
from homeworks.models import HomeworkAnswer


class IsHomeworkAnswerOwner(BasePermission):
    """
    Checks is user owns homework
    """
    def has_permission(self, request, view):
        homework_answer_id = request.parser_context['kwargs'].get(
            'homework_answer_pk')
        homework_id = request.parser_context['kwargs'].get('homework_pk')
        homework_answer = HomeworkAnswer.objects.get(pk=homework_answer_id)
        return homework_answer.user == request.user
        
        



