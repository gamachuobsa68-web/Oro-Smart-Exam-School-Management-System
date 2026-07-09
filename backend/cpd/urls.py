from django.urls import path

from .views import (
    CPDListView,
    CPDActivityView
)



urlpatterns = [

    path(
        "",
        CPDListView.as_view(),
        name="cpd-plans"
    ),


    path(
        "activities/",
        CPDActivityView.as_view(),
        name="cpd-activities"
    ),

]
