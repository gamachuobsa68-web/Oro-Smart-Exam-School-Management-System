from django.contrib import admin

from django.urls import (
    path,
    include
)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)



urlpatterns = [


    # Django Admin Panel
    path(
        "admin/",
        admin.site.urls
    ),



    # JWT Login
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token"
    ),



    # JWT Refresh
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh"
    ),



    # User Account System
    path(
        "api/accounts/",
        include(
            "accounts.urls"
        )
    ),



    # Exam System
    path(
        "api/exams/",
        include(
            "exams.urls"
        )
    ),



    # Report Card System
    path(
        "api/reports/",
        include(
            "reports.urls"
        )
    ),



    # Student Registration + Roster
    path(
        "api/students/",
        include(
            "students.urls"
        )
    ),



    # Teacher Assistant + Lesson Plan + CPD
    path(
        "api/professional/",
        include(
            "professional.urls"
        )
    ),
    path(
    "api/dashboard/",
    include(
        "dashboard.urls"
    )
),


]
