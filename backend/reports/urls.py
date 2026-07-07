from django.urls import path

from .views import (
    DownloadReportCardPDF
)



urlpatterns=[


    path(

        "download/<int:report_id>/",

        DownloadReportCardPDF.as_view(),

        name="download-report"

    ),


]
