from rest_framework import serializers

from quizes.models import Quiz, Question, AnswerOption


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['title', 'course', 'is_daily',
                  ]
        
        
class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['title', 'description', 'quiz',
                  'is_multianswered',
                  ]
        
        
class AnswerOptionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    
    class Meta:
        model = AnswerOption
        fields = ['description', 'question',
                  ]