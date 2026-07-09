from django.contrib import admin


from .models import (

    ReportCard,

    SchoolProfile

)





@admin.register(SchoolProfile)
class SchoolProfileAdmin(admin.ModelAdmin):


    list_display = (

        "name",

        "phone",

        "email"

    )


    search_fields = (

        "name",

        "phone"

    )







@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):


    list_display = (

        "student",

        "academic_year",

        "total_mark",

        "average",

        "rank",

        "grade",

        "status",

        "created_at"

    )


    list_filter = (

        "academic_year",

        "grade",

        "status"

    )


    search_fields = (

        "student__username",

        "student__first_name",

        "student__last_name"

    )


    readonly_fields = (

        "grade",

        "status",

        "created_at",

        "updated_at"

    )


    ordering = (

        "-created_at",

    )
