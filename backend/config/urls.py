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


    # Django Admin
    path(
        "admin/",
        admin.site.urls
    ),



    # JWT Login
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),



    # JWT Refresh Token
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),



    # User Accounts
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


]
