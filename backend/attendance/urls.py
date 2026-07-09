from django.urls import path


from .views import (

    TeacherAttendanceView,

    StudentAttendanceView,

    AdminAttendanceView

)



urlpatterns = [


    # Teacher mark and view attendance

    path(

        "teacher/",

        TeacherAttendanceView.as_view(),

        name="teacher-attendance"

    ),



    # Student view own attendance

    path(

        "student/",

        StudentAttendanceView.as_view(),

        name="student-attendance"

    ),



    # Admin view all attendance

    path(

        "admin/",

        AdminAttendanceView.as_view(),

        name="admin-attendance"

    ),

]
