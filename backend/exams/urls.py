from django.urls import path

from .views import (
    TeacherExamView,
    StudentExamView,
    StartExamView,
    SaveAnswerView,
    SubmitExamView,
)


urlpatterns = [

    # =========================
    # TEACHER EXAMS
    # Create and View Teacher Exams
    # =========================

    path(
        "teacher/exams/",
        TeacherExamView.as_view(),
        name="teacher-exams"
    ),


    # =========================
    # STUDENT EXAMS
    # View Published Exams
    # =========================

    path(
        "student/exams/",
        StudentExamView.as_view(),
        name="student-exams"
    ),


    # =========================
    # START EXAM
    # =========================

    path(
        "start/",
        StartExamView.as_view(),
        name="start-exam"
    ),


    # =========================
    # SAVE ANSWER
    # =========================

    path(
        "answers/save/",
        SaveAnswerView.as_view(),
        name="save-answer"
    ),


    # =========================
    # SUBMIT EXAM
    # =========================

    path(
        "submit/",
        SubmitExamView.as_view(),
        name="submit-exam"
    ),

]
