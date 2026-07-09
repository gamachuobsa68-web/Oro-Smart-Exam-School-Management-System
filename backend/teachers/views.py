from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Teacher

from .serializers import TeacherSerializer


from accounts.permissions import (
    IsAdmin,
    IsTeacher
)





# =========================
# TEACHER PROFILE
# =========================

class TeacherProfileView(APIView):


    permission_classes = [

        IsAuthenticated

    ]


    def get(self, request):

        try:

            teacher = Teacher.objects.get(

                user=request.user

            )


            serializer = TeacherSerializer(

                teacher

            )


            return Response(

                serializer.data

            )


        except Teacher.DoesNotExist:


            return Response(

                {
                    "message":
                    "Teacher profile not found"
                },

                status=404

            )





# =========================
# ADMIN VIEW ALL TEACHERS
# =========================

class TeacherListView(APIView):


    permission_classes = [

        IsAdmin

    ]


    def get(self, request):

        teachers = Teacher.objects.all()


        serializer = TeacherSerializer(

            teachers,

            many=True

        )


        return Response(

            serializer.data

        )





# =========================
# ADMIN CREATE TEACHER PROFILE
# =========================

class CreateTeacherView(APIView):


    permission_classes = [

        IsAdmin

    ]


    def post(self, request):

        serializer = TeacherSerializer(

            data=request.data

        )


        if serializer.is_valid():

            serializer.save()


            return Response(

                serializer.data,

                status=201

            )


        return Response(

            serializer.errors,

            status=400

        )





# =========================
# TEACHER DASHBOARD INFO
# =========================

class TeacherDashboardView(APIView):


    permission_classes = [

        IsTeacher

    ]


    def get(self, request):

        return Response(

            {

                "message":
                "Teacher Dashboard",

                "features":[

                    "Create Exam",

                    "Manage Questions",

                    "View Students",

                    "View Results",

                    "Manage Lesson Plans"

                ]

            }

        )
