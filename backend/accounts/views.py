from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .serializers import UserSerializer

from .permissions import (
    IsAdmin,
    IsTeacher,
    IsStudent
)



# User Profile
class ProfileView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        user = request.user

        return Response(
            UserSerializer(user).data
        )



# ADMIN DASHBOARD
class AdminDashboardView(APIView):

    permission_classes = [
        IsAdmin
    ]


    def get(self, request):

        return Response(
            {
                "role": "ADMIN",

                "message":
                "Welcome to Admin Dashboard",

                "permissions": [

                    "Manage Users",

                    "Manage Teachers",

                    "Manage Students",

                    "Control Server",

                    "View Reports",

                    "System Settings"

                ]
            }
        )



# TEACHER DASHBOARD
class TeacherDashboardView(APIView):

    permission_classes = [
        IsTeacher
    ]


    def get(self, request):

        return Response(
            {
                "role": "TEACHER",

                "message":
                "Welcome to Teacher Dashboard",

                "permissions": [

                    "Prepare Exam",

                    "Create Question",

                    "Upload Answer Key",

                    "Mark Students",

                    "Generate Report Card",

                    "Lesson Plan",

                    "Teacher Assistant",

                    "CPD Management"

                ]
            }
        )



# STUDENT DASHBOARD
class StudentDashboardView(APIView):

    permission_classes = [
        IsStudent
    ]


    def get(self, request):

        return Response(
            {
                "role": "STUDENT",

                "message":
                "Welcome to Student Dashboard",

                "permissions": [

                    "View Profile",

                    "Take Exam",

                    "Save Answer",

                    "Submit Exam",

                    "View Result",

                    "Download Report Card"

                ]
            }
        )
