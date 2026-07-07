from django.urls import path


from .views import (

    AdminDashboardView,

    TeacherDashboardView,

    StudentDashboardView

)



urlpatterns=[


    path(
        "admin/",
        AdminDashboardView.as_view()
    ),



    path(
        "teacher/",
        TeacherDashboardView.as_view()
    ),



    path(
        "student/",
        StudentDashboardView.as_view()
    ),

]
