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


    # =========================
    # DJANGO ADMIN
    # =========================

    path(

        "admin/",

        admin.site.urls

    ),





    # =========================
    # JWT AUTHENTICATION
    # =========================

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





    # =========================
    # ACCOUNTS
    # =========================

    path(

        "api/accounts/",

        include(
            "accounts.urls"
        )

    ),





    # =========================
    # TEACHERS
    # =========================

    path(

        "api/teachers/",

        include(
            "teachers.urls"
        )

    ),





    # =========================
    # STUDENTS
    # =========================

    path(

        "api/students/",

        include(
            "students.urls"
        )

    ),





    # =========================
    # EXAMS
    # =========================

    path(

        "api/exams/",

        include(
            "exams.urls"
        )

    ),





    # =========================
    # REPORTS
    # =========================

    path(

        "api/reports/",

        include(
            "reports.urls"
        )

    ),





    # =========================
    # SCHOOL MANAGEMENT
    # =========================

    path(

        "api/school/",

        include(
            "school.urls"
        )

    ),





    # =========================
    # PROFESSIONAL
    # =========================

    path(

        "api/professional/",

        include(
            "professional.urls"
        )

    ),





    # =========================
    # DASHBOARD
    # =========================

    path(

        "api/dashboard/",

        include(
            "dashboard.urls"
        )

    ),





    # =========================
    # CPD
    # =========================

    path(

        "api/cpd/",

        include(
            "cpd.urls"
        )

    ),

]





# =========================
# MEDIA FILES
# =========================

if settings.DEBUG:

    urlpatterns += static(

        settings.MEDIA_URL,

        document_root=settings.MEDIA_ROOT

    )
