from django.urls import path


from .views import (

    AdminReportView,

    TeacherReportView,

    StudentReportView,

    DownloadReportCardPDF

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


    path(
        "download/<int:report_id>/",
        DownloadReportCardPDF.as_view()
    ),

]
