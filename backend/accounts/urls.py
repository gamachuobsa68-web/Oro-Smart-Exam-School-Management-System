from django.urls import path


from .views import (

    RegisterView,

    ProfileView,

    AdminDashboardView,

    TeacherDashboardView,

    StudentDashboardView

)



urlpatterns = [


    # User Registration

    path(

        "register/",

        RegisterView.as_view(),

        name="register"

    ),



    # Current User Profile

    path(

        "profile/",

        ProfileView.as_view(),

        name="profile"

    ),



    # Admin Dashboard

    path(

        "admin-dashboard/",

        AdminDashboardView.as_view(),

        name="admin-dashboard"

    ),



    # Teacher Dashboard

    path(

        "teacher-dashboard/",

        TeacherDashboardView.as_view(),

        name="teacher-dashboard"

    ),



    # Student Dashboard

    path(

        "student-dashboard/",

        StudentDashboardView.as_view(),

        name="student-dashboard"

    ),

]
