from django.urls import path


from .views import (

    AdminDashboardView,

    TeacherDashboardView,

    StudentDashboardView

)



urlpatterns = [


    # Admin Dashboard

    path(

        "admin/",

        AdminDashboardView.as_view(),

        name="admin-dashboard"

    ),



    # Teacher Dashboard

    path(

        "teacher/",

        TeacherDashboardView.as_view(),

        name="teacher-dashboard"

    ),



    # Student Dashboard

    path(

        "student/",

        StudentDashboardView.as_view(),

        name="student-dashboard"

    ),

]
