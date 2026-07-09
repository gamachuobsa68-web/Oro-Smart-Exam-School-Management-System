from django.contrib import admin

from .models import (
    CPDPlan,
    CPDActivity
)





@admin.register(CPDPlan)
class CPDPlanAdmin(admin.ModelAdmin):

    list_display = (

        "title",

        "month",

        "created_at"

    )


    search_fields = (

        "title",

        "month"

    )


    list_filter = (

        "month",

    )


    ordering = (

        "-created_at",

    )





@admin.register(CPDActivity)
class CPDActivityAdmin(admin.ModelAdmin):

    list_display = (

        "teacher",

        "plan",

        "date",

        "status"

    )


    search_fields = (

        "teacher__username",

        "activity"

    )


    list_filter = (

        "status",

        "date"

    )


    ordering = (

        "-date",

    )
