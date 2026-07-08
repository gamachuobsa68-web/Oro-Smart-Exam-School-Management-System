from django.urls import path
from .views import DownloadReportCardPDF


urlpatterns = [
    path(
        "report-card/<int:student_id>/",
        DownloadReportCardPDF,
        name="download_report_card"
    ),
]
