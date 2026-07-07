from django.contrib import admin

from .models import ReportCard



@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):

    list_display = (

        "student",

        "academic_year",

        "total_mark",

        "average",

        "rank",

        "grade",

        "status"

    )


    list_filter = (

        "grade",

        "status",

    )
