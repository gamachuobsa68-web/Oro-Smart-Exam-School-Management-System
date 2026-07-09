from django.urls import path


from .views import (

    TeacherAssistantView,

    LessonPlanView,

    CPDView,

    CPDReportView

)



urlpatterns = [


    # Teacher Assistant

    path(

        "assistant/",

        TeacherAssistantView.as_view(),

        name="teacher-assistant"

    ),



    # Teacher Lesson Plan

    path(

        "lesson-plan/",

        LessonPlanView.as_view(),

        name="lesson-plan"

    ),



    # Teacher CPD

    path(

        "cpd/",

        CPDView.as_view(),

        name="teacher-cpd"

    ),



    # CPD Report

    path(

        "cpd-report/",

        CPDReportView.as_view(),

        name="cpd-report"

    ),

]
