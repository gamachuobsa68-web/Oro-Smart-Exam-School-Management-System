from django.db import models

from accounts.models import User

from school.models import (
    Subject,
    ClassRoom
)



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
        on_delete=models.CASCADE,
        related_name="exams_created"
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
        max_length=255
    )


    def __str__(self):

        return self.question_text





class ExamAttempt(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )


    started_at = models.DateTimeField(
        auto_now_add=True
    )


    submitted = models.BooleanField(
        default=False
    )


    submitted_at = models.DateTimeField(
        null=True,
        blank=True
    )


    def __str__(self):

        return (
            self.student.username
            + "-"
            + self.exam.title
        )





class StudentAnswer(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )


    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )


    answer = models.CharField(
        max_length=255
    )


    is_correct = models.BooleanField(
        default=False
    )


    mark_obtained = models.IntegerField(
        default=0
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.student.username





class ExamResult(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )


    total_mark = models.IntegerField(
        default=0
    )


    percentage = models.FloatField(
        default=0
    )


    grade = models.CharField(
        max_length=5,
        blank=True
    )


    status = models.CharField(
        max_length=20,
        default="FAIL"
    )


    submitted_at = models.DateTimeField(
        auto_now_add=True
    )


    def save(self, *args, **kwargs):

        if self.percentage >= 80:
            self.grade = "A"

        elif self.percentage >= 70:
            self.grade = "B"

        elif self.percentage >= 60:
            self.grade = "C"

        elif self.percentage >= 50:
            self.grade = "D"

        else:
            self.grade = "F"


        if self.percentage >= 50:
            self.status = "PASS"

        else:
            self.status = "FAIL"


        super().save(*args, **kwargs)



    def __str__(self):

        return self.student.username
