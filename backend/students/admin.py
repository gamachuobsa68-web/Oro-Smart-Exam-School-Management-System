from django.contrib import admin

from .models import StudentProfile



@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
change_list_template = "admin/students/studentprofile/change_list.html"

    list_display = (

        "student_id",

        "user",

        "classroom",

        "parent_name",

        "parent_phone",

        "is_active",

        "created_at"

    )


    list_filter = (

        "classroom",

        "is_active",

        "created_at"

    )


    search_fields = (

        "student_id",

        "user__username",

        "user__first_name",

        "user__last_name",

        "parent_name"

    )


    readonly_fields = (

        "created_at",

        "updated_at"

    )


    ordering = (

        "student_id",

    )
