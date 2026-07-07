from django.contrib import admin

from .models import (
    Exam,
    Question,
    StudentAnswer,
    ExamResult
)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "subject",
        "classroom",
        "teacher",
        "duration_minutes",
        "is_published"
    )

    list_filter = (
        "subject",
        "classroom",
        "is_published"
    )



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "exam",
        "question_type",
        "mark"
    )



@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "question",
        "is_correct",
        "mark_obtained"
    )



@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "exam",
        "total_mark",
        "percentage",
        "grade",
        "status"
    )

    list_filter = (
        "status",
        "grade"
    )
