from django.contrib import admin

from .models import (
    ReportCard,
    SchoolProfile
)



admin.site.register(
    SchoolProfile
)



@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):

    list_display = (

        "student",

        "academic_year",

        "average",

        "rank",

        "grade",

        "status"

    )
