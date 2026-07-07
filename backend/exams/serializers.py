from rest_framework import serializers

from .models import (
    Exam,
    Question,
    ExamAttempt,
    StudentAnswer,
    ExamResult
)



class QuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question

        fields = [
            "id",
            "exam",
            "question_text",
            "question_type",
            "mark",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "correct_answer",
        ]





class ExamSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(
        many=True,
        read_only=True
    )


    class Meta:

        model = Exam

        fields = [
            "id",
            "title",
            "subject",
            "classroom",
            "teacher",
            "exam_type",
            "duration_minutes",
            "total_mark",
            "is_published",
            "created_at",
            "questions",
        ]





class ExamAttemptSerializer(serializers.ModelSerializer):

    class Meta:

        model = ExamAttempt

        fields = [
            "id",
            "student",
            "exam",
            "started_at",
            "submitted",
            "submitted_at",
        ]





class StudentAnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudentAnswer

        fields = [
            "id",
            "student",
            "exam",
            "question",
            "answer",
            "is_correct",
            "mark_obtained",
            "created_at",
        ]





class ExamResultSerializer(serializers.ModelSerializer):

    class Meta:

        model = ExamResult

        fields = [
            "id",
            "student",
            "exam",
            "total_mark",
            "percentage",
            "grade",
            "status",
            "submitted_at",
        ]
