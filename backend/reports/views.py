from django.http import HttpResponse

from django.shortcuts import get_object_or_404


from reportlab.lib.pagesizes import A4

from reportlab.pdfgen import canvas


from students.models import StudentProfile


from .models import ReportCard





def DownloadReportCardPDF(request, student_id):


    student = get_object_or_404(

        StudentProfile,

        id=student_id

    )



    report = ReportCard.objects.filter(

        student=student.user

    ).last()





    response = HttpResponse(

        content_type="application/pdf"

    )


    response["Content-Disposition"] = (

        f'attachment; filename="report_card_{student_id}.pdf"'

    )



    pdf = canvas.Canvas(

        response,

        pagesize=A4

    )



    width, height = A4





    # Header

    pdf.setFont(

        "Helvetica-Bold",

        18

    )


    pdf.drawCentredString(

        width / 2,

        height - 70,

        "Oro Smart Exam School"

    )



    pdf.setFont(

        "Helvetica-Bold",

        14

    )


    pdf.drawCentredString(

        width / 2,

        height - 110,

        "Student Report Card"

    )





    # Student Information

    pdf.setFont(

        "Helvetica",

        12

    )


    y = height - 170



    pdf.drawString(

        70,

        y,

        f"Student ID: {student.student_id}"

    )


    pdf.drawString(

        70,

        y - 25,

        f"Student Name: {student.user.get_full_name()}"

    )


    pdf.drawString(

        70,

        y - 50,

        f"Class: {student.classroom}"

    )



    if report:


        pdf.drawString(

            70,

            y - 75,

            f"Academic Year: {report.academic_year}"

        )


    else:


        pdf.drawString(

            70,

            y - 75,

            "Academic Year: Not Available"

        )





    # Report Result

    y -= 140


    pdf.setFont(

        "Helvetica-Bold",

        12

    )


    pdf.drawString(

        70,

        y,

        "Total Mark"

    )


    pdf.drawString(

        220,

        y,

        "Average"

    )


    pdf.drawString(

        350,

        y,

        "Grade"

    )



    pdf.drawString(

        70,

        y - 30,

        str(report.total_mark if report else 0)

    )


    pdf.drawString(

        220,

        y - 30,

        str(report.average if report else 0)

    )


    pdf.drawString(

        350,

        y - 30,

        report.grade if report else "N/A"

    )





    pdf.drawString(

        70,

        y - 80,

        f"Status: {report.status if report else 'N/A'}"

    )



    pdf.drawString(

        70,

        y - 120,

        f"Teacher Comment: {report.teacher_comment if report else ''}"

    )



    pdf.drawString(

        70,

        y - 150,

        f"Principal Comment: {report.principal_comment if report else ''}"

    )





    pdf.drawString(

        70,

        y - 200,

        "Generated successfully."

    )



    pdf.showPage()

    pdf.save()



    return response
