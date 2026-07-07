from django.contrib import admin

from .models import StudentProfile



@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (

        "student_id",

        "user",

        "classroom",

        "parent_name",

        "parent_phone"

    )


    search_fields = (

        "student_id",

        "user__username"

    )
