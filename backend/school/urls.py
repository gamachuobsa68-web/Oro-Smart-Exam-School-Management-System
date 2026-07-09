from django.urls import path


from .views import (

    SchoolView,

    AcademicYearView,

    ClassRoomView,

    SubjectView

)



urlpatterns = [


    # School list + create

    path(

        "schools/",

        SchoolView.as_view(),

        name="schools"

    ),



    # Academic year list + create

    path(

        "academic-years/",

        AcademicYearView.as_view(),

        name="academic-years"

    ),



    # Classroom list + create

    path(

        "classrooms/",

        ClassRoomView.as_view(),

        name="classrooms"

    ),



    # Subject list + create

    path(

        "subjects/",

        SubjectView.as_view(),

        name="subjects"

    ),

]
