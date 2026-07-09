from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.permissions import (
    IsAdmin,
    IsTeacher
)

from .models import (
    CPDPlan,
    CPDActivity
)

from .serializers import (
    CPDPlanSerializer,
    CPDActivitySerializer
)



# =========================
# CPD PLAN
# =========================

class CPDListView(APIView):

    permission_classes = [
        IsAdmin
    ]


    def get(self, request):

        plans = CPDPlan.objects.all()

        serializer = CPDPlanSerializer(
            plans,
            many=True
        )

        return Response(
            serializer.data
        )


    def post(self, request):

        serializer = CPDPlanSerializer(
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
# CPD ACTIVITY
# =========================

class CPDActivityView(APIView):

    permission_classes = [
        IsTeacher
    ]


    def get(self, request):

        activities = CPDActivity.objects.filter(
            teacher=request.user
        )

        serializer = CPDActivitySerializer(
            activities,
            many=True
        )

        return Response(
            serializer.data
        )


    def post(self, request):

        serializer = CPDActivitySerializer(
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
