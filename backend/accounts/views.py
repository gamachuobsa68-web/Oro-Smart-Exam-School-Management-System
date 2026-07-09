from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import User

from .serializers import (
    UserSerializer,
    RegisterSerializer
)


from .permissions import (
    IsAdmin,
    IsTeacher,
    IsStudent
)





# =========================
# USER REGISTER
# =========================

class RegisterView(APIView):


    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )


        if serializer.is_valid():

            user = serializer.save()


            return Response(

                UserSerializer(user).data,

                status=201

            )


        return Response(

            serializer.errors,

            status=400

        )





# =========================
# USER PROFILE
# =========================

class ProfileView(APIView):


    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        return Response(

            UserSerializer(
                request.user
            ).data

        )




    def put(self, request):

        serializer = UserSerializer(

            request.user,

            data=request.data,

            partial=True

        )


        if serializer.is_valid():

            serializer.save()


            return Response(

                serializer.data

            )


        return Response(

            serializer.errors,

            status=400

        )





# =========================
# ADMIN DASHBOARD
# =========================

class AdminDashboardView(APIView):


    permission_classes = [

        IsAdmin

    ]


    def get(self, request):

        return Response({

            "role": "ADMIN",

            "message":
            "Welcome to Admin Dashboard",

            "permissions": [

                "Manage Users",

                "Manage Teachers",

                "Manage Students",

                "Manage Exams",

                "View Reports",

                "System Settings"

            ]

        })





# =========================
# TEACHER DASHBOARD
# =========================

class TeacherDashboardView(APIView):


    permission_classes = [

        IsTeacher

    ]


    def get(self, request):

        return Response({

            "role": "TEACHER",

            "message":
            "Welcome to Teacher Dashboard",

            "permissions": [

                "Create Exam",

                "Create Questions",

                "Publish Exam",

                "Mark Students",

                "View Results",

                "Lesson Plan",

                "CPD Management"

            ]

        })





# =========================
# STUDENT DASHBOARD
# =========================

class StudentDashboardView(APIView):


    permission_classes = [

        IsStudent

    ]


    def get(self, request):

        return Response({

            "role": "STUDENT",

            "message":
            "Welcome to Student Dashboard",

            "permissions": [

                "View Profile",

                "View Exams",

                "Take Exam",

                "Save Answer",

                "Submit Exam",

                "View Result",

                "Download Certificate"

            ]

        })
