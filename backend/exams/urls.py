from django.urls import path

from .views import (
    TeacherExamView,
    StudentExamView
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

]
