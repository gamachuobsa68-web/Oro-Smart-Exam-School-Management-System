from rest_framework.views import APIView

from rest_framework.response import Response


from .models import (

    TeacherAssistant,

    LessonPlan,

    CPD,

    CPDReport

)


from .serializers import (

    TeacherAssistantSerializer,

    LessonPlanSerializer,

    CPDSerializer,

    CPDReportSerializer

)


from accounts.permissions import (

    IsTeacher,

    IsAdmin

)





# ======================
# TEACHER ASSISTANT
# ======================

class TeacherAssistantView(APIView):

    permission_classes = [
        IsAdmin
    ]


    def get(self, request):

        data = TeacherAssistant.objects.all()

        serializer = TeacherAssistantSerializer(
            data,
            many=True
        )

        return Response(
            serializer.data
        )



    def post(self, request):

        serializer = TeacherAssistantSerializer(
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





# ======================
# LESSON PLAN
# ======================

class LessonPlanView(APIView):

    permission_classes = [
        IsTeacher
    ]


    def get(self, request):

        plans = LessonPlan.objects.filter(
            teacher=request.user
        )


        serializer = LessonPlanSerializer(
            plans,
            many=True
        )


        return Response(
            serializer.data
        )



    def post(self, request):

        serializer = LessonPlanSerializer(
            data=request.data
        )


        if serializer.is_valid():

            serializer.save(
                teacher=request.user
            )


            return Response(
                serializer.data,
                status=201
            )


        return Response(
            serializer.errors,
            status=400
        )





# ======================
# CPD
# ======================

class CPDView(APIView):

    permission_classes = [
        IsTeacher
    ]


    def get(self, request):

        cpd = CPD.objects.filter(
            teacher=request.user
        )


        serializer = CPDSerializer(
            cpd,
            many=True
        )


        return Response(
            serializer.data
        )



    def post(self, request):

        serializer = CPDSerializer(
            data=request.data
        )


        if serializer.is_valid():

            serializer.save(
                teacher=request.user
            )


            return Response(
                serializer.data,
                status=201
            )


        return Response(
            serializer.errors,
            status=400
        )





# ======================
# CPD MONTHLY REPORT
# ======================

class CPDReportView(APIView):

    permission_classes = [
        IsAdmin
    ]


    def get(self, request):

        reports = CPDReport.objects.all()


        serializer = CPDReportSerializer(
            reports,
            many=True
        )


        return Response(
            serializer.data
          )
