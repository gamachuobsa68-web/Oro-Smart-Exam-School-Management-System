from django.urls import path


from .views import (

    StudentListCreateView,

    StudentExcelImportView,

    ClassRosterView

)



urlpatterns = [


    # Admin student list and create
    path(
        "",
        StudentListCreateView.as_view(),
        name="students"
    ),



    # Import students from Excel
    path(
        "import-excel/",
        StudentExcelImportView.as_view(),
        name="student-import-excel"
    ),



    # Teacher class roster
    path(
        "roster/<int:classroom_id>/",
        ClassRosterView.as_view(),
        name="class-roster"
    ),


]
