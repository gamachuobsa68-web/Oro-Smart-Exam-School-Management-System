from django.contrib import admin

from .models import (
    School,
    AcademicYear,
    ClassRoom,
    Subject
)


admin.site.register(School)

admin.site.register(AcademicYear)

admin.site.register(ClassRoom)

admin.site.register(Subject)
