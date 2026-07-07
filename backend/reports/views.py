from django.db.models import Avg, Sum

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated


from .models import (
    ReportCard
)


from .serializers import (
    ReportCardSerializer
)


from accounts.permissions import (
    IsAdmin,
    IsTeacher,
    IsStudent
)





# ==========================
# ADMIN VIEW ALL REPORT
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

            report = serializer.save()


            self.calculate_rank()


            return Response(
                ReportCardSerializer(report).data,
                status=201
            )


        return Response(
            serializer.errors,
            status=400
        )



    def calculate_rank(self):

        reports = ReportCard.objects.all().order_by(
            "-average"
        )


        rank = 1


        for report in reports:

            report.rank = rank

            report.save(
                update_fields=[
                    "rank"
                ]
            )

            rank += 1





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
