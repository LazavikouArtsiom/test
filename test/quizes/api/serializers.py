from rest_framework import serializers

from quizes.models import Quiz, Question, AnswerOption


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = "__all__"
        
        
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"
        
        
class AnswerOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerOption
        fields = "__all__"