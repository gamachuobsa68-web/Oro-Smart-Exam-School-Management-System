from django.urls import path


from .views import (

    AdminReportView,

    TeacherReportView,

    StudentReportView

)



urlpatterns = [


    path(

        "admin/",

        AdminReportView.as_view()

    ),



    path(

        "teacher/",

        TeacherReportView.as_view()

    ),



    path(

        "student/",

        StudentReportView.as_view()

    ),


]
