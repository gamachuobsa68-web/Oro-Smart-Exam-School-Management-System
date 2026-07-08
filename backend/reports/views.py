from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from students.models import StudentProfile


def DownloadReportCardPDF(request, student_id):

    student = get_object_or_404(
        StudentProfile,
        id=student_id
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = f'attachment; filename="report_card_{student_id}.pdf"'


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
        height - 80,
        "Oro Smart Exam School"
    )


    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawCentredString(
        width / 2,
        height - 120,
        "Student Report Card"
    )


    # Student information
    pdf.setFont(
        "Helvetica",
        12
    )

    y = height - 180


    pdf.drawString(
        80,
        y,
        f"Student ID: {student.student_id}"
    )


    pdf.drawString(
        80,
        y - 30,
        f"Student Name: {student.user}"
    )


    pdf.drawString(
        80,
        y - 60,
        f"Class: {student.classroom}"
    )


    pdf.drawString(
        80,
        y - 90,
        "Academic Year: __________"
    )


    # Table header
    y = y - 150

    pdf.setFont(
        "Helvetica-Bold",
        12
    )

    pdf.drawString(80, y, "Subject")
    pdf.drawString(250, y, "Mark")
    pdf.drawString(350, y, "Grade")


    pdf.setFont(
        "Helvetica",
        12
    )


    subjects = [
        ("Mathematics", ""),
        ("English", ""),
        ("Science", ""),
    ]


    y -= 30


    for subject, mark in subjects:

        pdf.drawString(
            80,
            y,
            subject
        )

        pdf.drawString(
            250,
            y,
            mark
        )

        pdf.drawString(
            350,
            y,
            ""
        )

        y -= 25


    pdf.drawString(
        80,
        y - 30,
        "Generated successfully."
    )


    pdf.showPage()
    pdf.save()

    return response
