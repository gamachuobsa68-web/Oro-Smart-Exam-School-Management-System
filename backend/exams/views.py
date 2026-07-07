from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Exam

from .serializers import ExamSerializer

from accounts.permissions import (
    IsTeacher,
    IsStudent
)



# Teacher Exam List/Create

class TeacherExamView(APIView):

    permission_classes = [
        IsTeacher
    ]


    def get(self, request):

        exams = Exam.objects.filter(
            teacher=request.user
        )

        serializer = ExamSerializer(
            exams,
            many=True
        )

        return Response(
            serializer.data
        )


    def post(self, request):

        serializer = ExamSerializer(
            data=request.data
        )


        if serializer.is_valid():

            serializer.save(
                teacher=request.user
            )

            return Response(
                serializer.data
            )


        return Response(
            serializer.errors,
            status=400
        )



# Student Exam List

class StudentExamView(APIView):

    permission_classes = [
        IsStudent
    ]


    def get(self, request):

        exams = Exam.objects.filter(
            is_published=True
        )


        serializer = ExamSerializer(
            exams,
            many=True
        )


        return Response(
            serializer.data
  )
