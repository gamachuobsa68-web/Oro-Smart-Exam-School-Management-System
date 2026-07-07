from django.urls import path


from .views import (

    TeacherAssistantView,

    LessonPlanView,

    CPDView,

    CPDReportView

)



urlpatterns = [


    path(
        "assistant/",
        TeacherAssistantView.as_view()
    ),



    path(
        "lesson-plan/",
        LessonPlanView.as_view()
    ),



    path(
        "cpd/",
        CPDView.as_view()
    ),



    path(
        "cpd-report/",
        CPDReportView.as_view()
    ),

]
