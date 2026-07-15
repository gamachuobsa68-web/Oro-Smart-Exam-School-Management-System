from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect

from .models import StudentProfile
from .utils.excel_import import import_students_excel


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
        "created_at",
    )

    list_filter = (
        "classroom",
        "is_active",
        "created_at",
    )

    search_fields = (
        "student_id",
        "user__username",
        "user__first_name",
        "user__last_name",
        "parent_name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "student_id",
    )


    def get_urls(self):

        urls = super().get_urls()

        custom_urls = [
            path(
                "import-excel/",
                self.admin_site.admin_view(self.import_excel),
                name="student-import-excel",
            ),
        ]

        return custom_urls + urls


    def import_excel(self, request):

        if request.method == "POST":

            excel_file = request.FILES.get("excel_file")

            if excel_file:

                import_students_excel(excel_file)

                self.message_user(
                    request,
                    "Students imported successfully."
                )

                return redirect(
                    "admin:students_studentprofile_changelist"
                )


        return render(
            request,
            "admin/import_excel.html"
        )