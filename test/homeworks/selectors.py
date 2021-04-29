from django.shortcuts import get_list_or_404, get_object_or_404
from homeworks.models import HomeworkAnswer, HomeworkReview, Homework

def get_homeworks_list(self, request):
    lesson_id = self.request.parser_context['kwargs'].get('lessons_pk')
    return get_list_or_404(Homework.objects
                           .select_related('lesson'))
    
    
def get_homework_answers_detail(self, request):
    homework_id = self.request.parser_context['kwargs'].get('homeworks_pk')
    return get_object_or_404(
        HomeworkAnswer.objects.select_related('user', 'homework'),
        user=request.user,
        homework_id=homework_id,
    )


def get_homework_answers_list(self, request):
    homework_id = self.request.parser_context['kwargs'].get('homeworks_pk')
    return get_list_or_404(
        HomeworkAnswer.objects.select_related('user', 'homework'),
        homework_id=homework_id,
    )


def get_homework_review_detail(self):
    homework_answer_id = self.request.parser_context['kwargs'].get(
        'homework_answers_pk')
    return get_object_or_404(
        HomeworkReview.objects.select_related('homework_answer'),
        homework_answer_id=homework_answer_id,
        )

