from django.contrib import admin

from django.urls import (
    path,
    include
)

from django.conf import settings

from django.conf.urls.static import static


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)





urlpatterns = [


    # ADMIN PANEL

    path(
        "admin/",
        admin.site.urls
    ),



    # JWT

    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token"
    ),


    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh"
    ),



    # ACCOUNTS

    path(
        "api/accounts/",
        include(
            "accounts.urls"
        )
    ),



    # TEACHERS

    path(
        "api/teachers/",
        include(
            "teachers.urls"
        )
    ),



    # STUDENTS

    path(
        "api/students/",
        include(
            "students.urls"
        )
    ),



    # SCHOOL

    path(
        "api/school/",
        include(
            "school.urls"
        )
    ),



    # EXAMS

    path(
        "api/exams/",
        include(
            "exams.urls"
        )
    ),



    # REPORTS

    path(
        "api/reports/",
        include(
            "reports.urls"
        )
    ),



    # PROFESSIONAL

    path(
        "api/professional/",
        include(
            "professional.urls"
        )
    ),



    # DASHBOARD

    path(
        "api/dashboard/",
        include(
            "dashboard.urls"
        )
    ),



    # CPD

    path(
        "api/cpd/",
        include(
            "cpd.urls"
        )
    ),



    # ATTENDANCE

    path(
        "api/attendance/",
        include(
            "attendance.urls"
        )
    ),



    # ASSISTANT

    path(
        "api/assistant/",
        include(
            "assistant.urls"
        )
    ),

]





# MEDIA FILES

if settings.DEBUG:

    urlpatterns += static(

        settings.MEDIA_URL,

        document_root=settings.MEDIA_ROOT

    )
