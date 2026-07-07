from django.urls import path

from .views import (
    ProfileView,
    AdminDashboardView,
    TeacherDashboardView,
    StudentDashboardView
)



urlpatterns = [


    path(
        "profile/",
        ProfileView.as_view()
    ),


    path(
        "admin-dashboard/",
        AdminDashboardView.as_view()
    ),


    path(
        "teacher-dashboard/",
        TeacherDashboardView.as_view()
    ),


    path(
        "student-dashboard/",
        StudentDashboardView.as_view()
    ),

]
