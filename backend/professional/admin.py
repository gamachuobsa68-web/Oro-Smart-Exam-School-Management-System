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

        "phone",

        "created_at"

    )


    search_fields = (

        "teacher__username",

        "qualification",

        "specialization"

    )





@admin.register(LessonPlan)
class LessonPlanAdmin(admin.ModelAdmin):


    list_display = (

        "teacher",

        "subject",

        "classroom",

        "topic",

        "date",

        "created_at"

    )


    list_filter = (

        "subject",

        "classroom",

        "date"

    )


    search_fields = (

        "teacher__username",

        "topic"

    )





@admin.register(CPD)
class CPDAdmin(admin.ModelAdmin):


    list_display = (

        "teacher",

        "title",

        "month",

        "hours",

        "status",

        "created_at"

    )


    list_filter = (

        "month",

        "status"

    )


    search_fields = (

        "teacher__username",

        "title"

    )





@admin.register(CPDReport)
class CPDReportAdmin(admin.ModelAdmin):


    list_display = (

        "teacher",

        "month",

        "completed_cpd",

        "total_hours",

        "created_at"

    )


    list_filter = (

        "month",

    )


    search_fields = (

        "teacher__username",

    )
