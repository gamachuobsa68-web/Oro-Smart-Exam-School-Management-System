from django.http import HttpResponse

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated


from reportlab.pdfgen import canvas


from .models import (
    ReportCard,
    SchoolProfile
)



from accounts.permissions import IsStudent





class DownloadReportCardPDF(APIView):

    permission_classes=[
        IsStudent
    ]


    def get(self,request,report_id):

        report = ReportCard.objects.get(
            id=report_id,
            student=request.user
        )


        school = SchoolProfile.objects.first()



        response = HttpResponse(
            content_type="application/pdf"
        )


        response[
            "Content-Disposition"
        ] = (
            'attachment; filename="report_card.pdf"'
        )



        pdf = canvas.Canvas(
            response
        )



        y = 800



        if school:

            pdf.setFont(
                "Helvetica-Bold",
                18
            )

            pdf.drawCentredString(
                300,
                y,
                school.name
            )

            y -=40



        pdf.setFont(
            "Helvetica",
            12
        )


        pdf.drawString(
            50,
            y,
            "OFFICIAL REPORT CARD"
        )


        y -=40



        pdf.drawString(
            50,
            y,
            "Student: "
            + report.student.username
        )


        y -=30



        pdf.drawString(
            50,
            y,
            "Total Mark: "
            + str(report.total_mark)
        )


        y -=30



        pdf.drawString(
            50,
            y,
            "Average: "
            + str(report.average)
        )


        y -=30



        pdf.drawString(
            50,
            y,
            "Rank: "
            + str(report.rank)
        )


        y -=30



        pdf.drawString(
            50,
            y,
            "Grade: "
            + report.grade
        )


        y -=30



        pdf.drawString(
            50,
            y,
            "Status: "
            + report.status
        )


        y -=40



        pdf.drawString(
            50,
            y,
            "Teacher Comment:"
        )


        y -=20


        pdf.drawString(
            70,
            y,
            report.teacher_comment
        )



        y -=40



        pdf.drawString(
            50,
            y,
            "Principal Comment:"
        )


        y -=20


        pdf.drawString(
            70,
            y,
            report.principal_comment
        )



        pdf.save()



        return response
