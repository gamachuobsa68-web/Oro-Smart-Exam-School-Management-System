from django.contrib import admin


from .models import (
    School,
    AcademicYear,
    ClassRoom,
    Subject,
    Grade,
    SchoolSetting
)





@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):


    list_display = (

        "name",

        "phone",

        "email",

        "created_at"

    )


    search_fields = (

        "name",

        "phone"

    )





@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):


    list_display = (

        "name",

        "start_date",

        "end_date",

        "is_current"

    )


    list_filter = (

        "is_current",

    )





@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):


    list_display = (

        "name",

        "section",

        "school",

        "academic_year",

        "capacity"

    )


    list_filter = (

        "school",

        "academic_year"

    )


    search_fields = (

        "name",

        "section"

    )





@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):


    list_display = (

        "name",

        "code",

        "is_active"

    )


    list_filter = (

        "is_active",

    )


    search_fields = (

        "name",

        "code"

    )
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )



@admin.register(SchoolSetting)
class SchoolSettingAdmin(admin.ModelAdmin):

    list_display = (
        "school",
        "report_title",
        "principal_name",
        "teacher_name",
    )

    search_fields = (
        "school__name",
    )
