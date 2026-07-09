from django.urls import path


from .views import (

    StudentListCreateView,

    StudentProfileView,

    StudentExcelImportView,

    ClassRosterView

)



urlpatterns = [


    # Admin student list + create

    path(

        "",

        StudentListCreateView.as_view(),

        name="students"

    ),



    # Student own profile

    path(

        "profile/",

        StudentProfileView.as_view(),

        name="student-profile"

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
