from django.urls import path

from .views import (
    TeacherExamView,
    StudentExamView,
    StartExamView,
    SaveAnswerView,
    SubmitExamView,
)



urlpatterns = [

    # Teacher create and view exams
    path(
        "teacher/",
        TeacherExamView.as_view(),
        name="teacher-exams"
    ),


    # Student view published exams
    path(
        "student/",
        StudentExamView.as_view(),
        name="student-exams"
    ),


    # Student start exam
    path(
        "start/",
        StartExamView.as_view(),
        name="start-exam"
    ),


    # Save answer button
    path(
        "save-answer/",
        SaveAnswerView.as_view(),
        name="save-answer"
    ),


    # Submit exam
    path(
        "submit/",
        SubmitExamView.as_view(),
        name="submit-exam"
    ),

]
