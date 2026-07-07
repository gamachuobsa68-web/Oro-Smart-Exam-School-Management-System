from django.contrib import admin

from .models import (
    Exam,
    Question,
    ExamAttempt,
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
        "exam_type",
        "duration_minutes",
        "is_published",
    )


    list_filter = (
        "exam_type",
        "subject",
        "classroom",
        "is_published",
    )


    search_fields = (
        "title",
    )




@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "exam",
        "question_type",
        "mark",
    )


    list_filter = (
        "question_type",
        "exam",
    )



@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "exam",
        "started_at",
        "submitted",
        "submitted_at",
    )


    list_filter = (
        "submitted",
    )



@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "exam",
        "question",
        "is_correct",
        "mark_obtained",
    )


    list_filter = (
        "is_correct",
    )



@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "exam",
        "total_mark",
        "percentage",
        "grade",
        "status",
    )


    list_filter = (
        "grade",
        "status",
    )
