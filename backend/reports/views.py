from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated


from .models import ReportCard

from .serializers import ReportCardSerializer


from accounts.permissions import (
    IsAdmin,
    IsTeacher,
    IsStudent
)



# ==========================
# ADMIN VIEW ALL REPORTS
# ==========================

class AdminReportView(APIView):

    permission_classes = [
        IsAdmin
    ]


    def get(self, request):

        reports = ReportCard.objects.all()


        serializer = ReportCardSerializer(
            reports,
            many=True
        )


        return Response(
            serializer.data
        )





# ==========================
# TEACHER CREATE REPORT
# ==========================

class TeacherReportView(APIView):

    permission_classes = [
        IsTeacher
    ]


    def get(self, request):

        reports = ReportCard.objects.all()


        serializer = ReportCardSerializer(
            reports,
            many=True
        )


        return Response(
            serializer.data
        )



    def post(self, request):

        serializer = ReportCardSerializer(
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
# STUDENT VIEW OWN REPORT
# ==========================

class StudentReportView(APIView):

    permission_classes = [
        IsStudent
    ]


    def get(self, request):

        reports = ReportCard.objects.filter(

            student=request.user

        )


        serializer = ReportCardSerializer(
            reports,
            many=True
        )


        return Response(
            serializer.data
        )
