from rest_framework import serializers

from .models import (
    Exam,
    Question,
    StudentAnswer,
    ExamResult
)



class QuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question

        fields = "__all__"





class ExamSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(
        many=True,
        read_only=True
    )


    class Meta:

        model = Exam

        fields = "__all__"





class StudentAnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudentAnswer

        fields = "__all__"





class ExamResultSerializer(serializers.ModelSerializer):

    class Meta:

        model = ExamResult

        fields = "__all__"
