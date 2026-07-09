from django.urls import path


from .views import (

    DownloadReportCardPDF,

)



urlpatterns = [


    # Download student report card PDF

    path(

        "report-card/<int:student_id>/",

        DownloadReportCardPDF,

        name="download-report-card"

    ),


]
