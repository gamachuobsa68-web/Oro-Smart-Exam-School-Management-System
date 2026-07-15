from django.db import models
from accounts.models import User
from school.models import Subject, ClassRoom


class Exam(models.Model):

    EXAM_TYPES = (
        ("ONLINE", "Online"),
        ("PAPER", "Paper"),
    )

    STATUS = (
        ("DRAFT", "Draft"),
        ("PUBLISHED", "Published"),
        ("CLOSED", "Closed"),
    )

    title = models.CharField(max_length=200)

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="exams"
    )

    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        related_name="exams"
    )

    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_exams"
    )

    exam_type = models.CharField(
        max_length=20,
        choices=EXAM_TYPES,
        default="ONLINE"
    )

    duration_minutes = models.PositiveIntegerField(default=60)

    total_mark = models.PositiveIntegerField(default=100)

    pass_mark = models.PositiveIntegerField(default=50)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="DRAFT"
    )

    is_published = models.BooleanField(default=False)

    start_time = models.DateTimeField(
        null=True,
        blank=True
    )

    end_time = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.title



class Question(models.Model):

    QUESTION_TYPES = (
        ("MCQ", "Multiple Choice"),
        ("TEXT", "Written"),
    )


    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="questions"
    )


    question_text = models.TextField()


    question_type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPES,
        default="MCQ"
    )


    mark = models.PositiveIntegerField(
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



class ExamAttempt(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="exam_attempts"
    )


    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="attempts"
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
        return self.student.username + " - " + self.exam.title



class StudentAnswer(models.Model):

    attempt = models.ForeignKey(
        ExamAttempt,
        on_delete=models.CASCADE,
        related_name="answers",
        null=True,
        blank=True
    )


    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )


    answer = models.CharField(
        max_length=255,
        blank=True
    )


    is_correct = models.BooleanField(
        default=False
    )


    mark_obtained = models.PositiveIntegerField(
        default=0
    )


    def __str__(self):
        return self.attempt.student.username



class ExamResult(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="exam_results"
    )


    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="results"
    )


    total_mark = models.PositiveIntegerField(
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


    rank = models.PositiveIntegerField(
        null=True,
        blank=True
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
        return self.student.username + " - " + self.exam.title