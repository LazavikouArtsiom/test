from django.db import transaction

from rest_framework import serializers

from homeworks.models import Homework, HomeworkAnswer


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"


class HomeworkAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkAnswer
        fields = ['user', 'homework', 'text']
