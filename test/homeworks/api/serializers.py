from django.db import transaction

from rest_framework import serializers

from homeworks.models import Homework, HomeworkAnswer, HomeworkReview


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ["id", "lesson", "title", "description"]


class HomeworkAnswerSerializer(serializers.ModelSerializer):
    homework = HomeworkSerializer(read_only=True)

    class Meta:
        model = HomeworkAnswer
        fields = ["id", "user", "homework", "text"]


class HomeworkReviewSerializer(serializers.ModelSerializer):
    homework_answer = HomeworkAnswerSerializer(read_only=True)
    
    class Meta:
        model = HomeworkReview
        fields = ["id", "score", "review_text", "homework_answer"]
