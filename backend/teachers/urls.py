from django.urls import path


from .views import (

    TeacherProfileView,

    TeacherListView,

    CreateTeacherView,

    TeacherDashboardView,

)



urlpatterns = [


    # Teacher own profile

    path(

        "profile/",

        TeacherProfileView.as_view(),

        name="teacher-profile"

    ),



    # Admin view all teachers

    path(

        "list/",

        TeacherListView.as_view(),

        name="teacher-list"

    ),



    # Admin create teacher profile

    path(

        "create/",

        CreateTeacherView.as_view(),

        name="teacher-create"

    ),



    # Teacher dashboard

    path(

        "dashboard/",

        TeacherDashboardView.as_view(),

        name="teacher-dashboard"

    ),


]
