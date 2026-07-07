from rest_framework.views import APIView

from rest_framework.response import Response


from accounts.permissions import (

    IsAdmin,

    IsTeacher,

    IsStudent

)



class AdminDashboardView(APIView):

    permission_classes = [
        IsAdmin
    ]


    def get(self, request):

        return Response({

            "role":"ADMIN",

            "message":
            "Admin control panel",

            "permissions":[

                "Manage users",

                "Manage exams",

                "Manage reports",

                "Server control"

            ]

        })





class TeacherDashboardView(APIView):

    permission_classes = [
        IsTeacher
    ]


    def get(self, request):

        return Response({

            "role":"TEACHER",

            "message":
            "Teacher dashboard",

            "permissions":[

                "Prepare exam",

                "Lesson plan",

                "CPD",

                "View roster"

            ]

        })





class StudentDashboardView(APIView):

    permission_classes = [
        IsStudent
    ]


    def get(self, request):

        return Response({

            "role":"STUDENT",

            "message":
            "Student dashboard",

            "permissions":[

                "Take exam",

                "View result",

                "Download report card"

            ]

        })
