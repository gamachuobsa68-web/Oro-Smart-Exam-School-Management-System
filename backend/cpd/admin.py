from django.contrib import admin
from .models import CPDPlan, CPDActivity


@admin.register(CPDPlan)
class CPDPlanAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "month",
        "created_at"
    )


@admin.register(CPDActivity)
class CPDActivityAdmin(admin.ModelAdmin):
    list_display = (
        "teacher",
        "activity",
        "date",
        "status"
    )
