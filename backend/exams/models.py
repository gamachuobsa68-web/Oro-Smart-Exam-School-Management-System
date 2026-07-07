from django.db import models

from school.models import (
    Subject,
    ClassRoom
)

from accounts.models import User



class Exam(models.Model):

    EXAM_TYPES = (

        ("ONLINE", "Online"),

        ("PAPER", "Paper"),

    )


    title = models.CharField(
        max_length=200
    )


    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )


    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )


    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    exam_type = models.CharField(
        max_length=20,
        choices=EXAM_TYPES,
        default="ONLINE"
    )


    duration_minutes = models.IntegerField(
        default=60
    )


    total_mark = models.IntegerField(
        default=100
    )


    is_published = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title





class Question(models.Model):


    QUESTION_TYPES = (

        ("MCQ", "Multiple Choice"),

        ("TEXT", "Written Answer"),

    )


    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="questions"
    )


    question_text = models.TextField()


    question_type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPES
    )


    mark = models.IntegerField(
        default=1
    )


    option_a = models.CharField(
        max_length=255,
        blank=True
    )


    option_b = models.CharField(
        max_length=255,
        blank=True
    )


    option_c = models.CharField(
        max_length=255,
        blank=True
    )


    option_d = models.CharField(
        max_length=255,
        blank=True
    )


    correct_answer = models.CharField(
        max_length=255,
        blank=True
    )


    def __str__(self):

        return self.question_text
