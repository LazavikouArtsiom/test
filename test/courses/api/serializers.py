from rest_framework import serializers

from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'title', 'description']
        
        
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title', 'description', 'course']
