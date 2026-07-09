from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Attendance


from .serializers import AttendanceSerializer


from accounts.permissions import (
    IsAdmin,
    IsTeacher,
    IsStudent
)





# =========================
# TEACHER MARK ATTENDANCE
# =========================

class TeacherAttendanceView(APIView):

    permission_classes = [

        IsTeacher

    ]



    def get(self, request):

        records = Attendance.objects.filter(

            marked_by=request.user

        )


        serializer = AttendanceSerializer(

            records,

            many=True

        )


        return Response(

            serializer.data

        )




    def post(self, request):

        serializer = AttendanceSerializer(

            data=request.data

        )


        if serializer.is_valid():

            serializer.save(

                marked_by=request.user

            )


            return Response(

                serializer.data,

                status=201

            )


        return Response(

            serializer.errors,

            status=400

        )








# =========================
# STUDENT VIEW ATTENDANCE
# =========================

class StudentAttendanceView(APIView):

    permission_classes = [

        IsStudent

    ]



    def get(self, request):


        records = Attendance.objects.filter(

            student=request.user

        )


        serializer = AttendanceSerializer(

            records,

            many=True

        )


        return Response(

            serializer.data

        )








# =========================
# ADMIN VIEW ALL ATTENDANCE
# =========================

class AdminAttendanceView(APIView):

    permission_classes = [

        IsAdmin

    ]



    def get(self, request):


        records = Attendance.objects.all()


        serializer = AttendanceSerializer(

            records,

            many=True

        )


        return Response(

            serializer.data

  )
