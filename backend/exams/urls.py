from django.urls import path

from .views import (
    TeacherExamView,
    StudentExamView,
    SubmitExamView
)



urlpatterns = [


    path(
        "teacher/",
        TeacherExamView.as_view()
    ),


    path(
        "student/",
        StudentExamView.as_view()
    ),


    path(
        "submit/",
        SubmitExamView.as_view()
    ),

]
