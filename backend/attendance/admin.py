from django.contrib import admin


from .models import Attendance





@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):


    list_display = (

        "student",

        "classroom",

        "date",

        "status",

        "marked_by"

    )


    list_filter = (

        "status",

        "date",

        "classroom"

    )


    search_fields = (

        "student__username",

        "marked_by__username"

    )


    ordering = (

        "-date",

    )
