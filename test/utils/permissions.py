from rest_framework.permissions import BasePermission

from courses.models import Course


class IsSubscribed(BasePermission):
    """
    Checks is user subscribed to course
    """
    def has_permission(self, request, view):
        course_id = request.parser_context['kwargs'].get(
            'pk') or request.parser_context['kwargs'].get('courses_pk')
        course = Course.objects.get(pk=course_id)
        return course in request.user.courses.all()


class IsSubscribedOrIsAdmin(BasePermission):
    """
    Checks is user subscribed to course
    """
    def has_permission(self, request, view):
        course_id = request.parser_context['kwargs'].get(
            'pk') or request.parser_context['kwargs'].get('courses_pk')
        course = Course.objects.get(pk=course_id)
        return (course in request.user.courses.all()) or bool(
            request.user and request.user.is_staff)
