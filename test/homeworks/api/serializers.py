from django.db import transaction

from rest_framework import serializers

from homeworks.models import Homework, HomeworkAnswer, HomeworkReview


# class HomeworkFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HomeworkFile
#         fields = ["homework_file"]


class HomeworkSerializer(serializers.ModelSerializer):
    # homework_files = HomeworkFileSerializer(read_only=True)

    class Meta:
        model = Homework
        fields = ["id", "lesson", "title", "description"]


class HomeworkAnswerSerializer(serializers.ModelSerializer):
    homework = HomeworkSerializer(read_only=True)

    class Meta:
        model = HomeworkAnswer
        fields = ["id", "user", "homework", "text"]


class HomeworkReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeworkReview
        fields = ["id", "score", "review_text", "homework_answer"]
