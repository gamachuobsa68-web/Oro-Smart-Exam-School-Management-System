from django.contrib import admin

from .models import Teacher



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):


    list_display = (

        "user",

        "employee_id",

        "is_active",

        "created_at"

    )


    list_filter = (

        "is_active",

    )


    search_fields = (

        "user__username",

        "employee_id",

        "user__first_name",

        "user__last_name"

    )


    filter_horizontal = (

        "subjects",

        "classrooms",

    )
