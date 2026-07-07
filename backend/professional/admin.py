from django.contrib import admin

from .models import (
    TeacherAssistant,
    LessonPlan,
    CPD,
    CPDReport
)



@admin.register(TeacherAssistant)
class TeacherAssistantAdmin(admin.ModelAdmin):

    list_display = (
        "teacher",
        "qualification",
        "specialization",
        "phone"
    )



@admin.register(LessonPlan)
class LessonPlanAdmin(admin.ModelAdmin):

    list_display = (
        "teacher",
        "subject",
        "classroom",
        "topic",
        "date"
    )

    list_filter = (
        "subject",
        "classroom"
    )



@admin.register(CPD)
class CPDAdmin(admin.ModelAdmin):

    list_display = (
        "teacher",
        "title",
        "month",
        "hours",
        "status"
    )

    list_filter = (
        "month",
        "status"
    )



@admin.register(CPDReport)
class CPDReportAdmin(admin.ModelAdmin):

    list_display = (
        "teacher",
        "month",
        "completed_cpd",
        "total_hours"
    )
