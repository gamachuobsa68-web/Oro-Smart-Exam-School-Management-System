from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth import get_user_model


import openpyxl


from .models import StudentProfile

from .serializers import StudentSerializer


from accounts.permissions import (
    IsAdmin,
    IsTeacher,
    IsStudent
)



User = get_user_model()





# ==========================
# STUDENT LIST + CREATE
# ==========================

class StudentListCreateView(APIView):


    permission_classes = [

        IsAdmin

    ]



    def get(self, request):

        students = StudentProfile.objects.all()


        serializer = StudentSerializer(

            students,

            many=True

        )


        return Response(

            serializer.data

        )





    def post(self, request):

        serializer = StudentSerializer(

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







# ==========================
# MY STUDENT PROFILE
# ==========================

class StudentProfileView(APIView):


    permission_classes = [

        IsStudent

    ]



    def get(self, request):

        try:

            student = StudentProfile.objects.get(

                user=request.user

            )


            serializer = StudentSerializer(

                student

            )


            return Response(

                serializer.data

            )


        except StudentProfile.DoesNotExist:


            return Response(

                {
                    "message":
                    "Student profile not found"
                },

                status=404

            )







# ==========================
# CLASS ROSTER
# ==========================

class ClassRosterView(APIView):


    permission_classes = [

        IsTeacher

    ]



    def get(self, request, classroom_id):


        students = StudentProfile.objects.filter(

            classroom_id=classroom_id

        )


        serializer = StudentSerializer(

            students,

            many=True

        )


        return Response(

            serializer.data

        )







# ==========================
# EXCEL IMPORT
# ==========================

class StudentExcelImportView(APIView):


    permission_classes = [

        IsAdmin

    ]



    def post(self, request):


        excel_file = request.FILES.get(

            "file"

        )


        if not excel_file:


            return Response(

                {
                    "error":
                    "Excel file required"
                },

                status=400

            )



        workbook = openpyxl.load_workbook(

            excel_file

        )


        sheet = workbook.active



        created = 0



        for row in sheet.iter_rows(

            min_row=2,

            values_only=True

        ):



            username = row[0]

            student_id = row[1]

            classroom_id = row[2]

            parent_name = row[3]

            parent_phone = row[4]



            if User.objects.filter(

                username=username

            ).exists():

                continue



            user = User.objects.create_user(

                username=username,

                password="student123",

                role="STUDENT"

            )



            StudentProfile.objects.create(

                user=user,

                student_id=student_id,

                classroom_id=classroom_id,

                parent_name=parent_name,

                parent_phone=parent_phone

            )


            created += 1



        return Response(

            {

                "message":

                "Students imported successfully",

                "total":

                created

            }

        )
