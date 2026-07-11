from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    CPDPlan,
    CPDActivity
)



class CPDListView(APIView):

    def get(self, request):

        plans = CPDPlan.objects.all()

        data = []

        for plan in plans:

            data.append({

                "id": plan.id,

                "title": plan.title,

                "description": plan.description,

                "month": plan.month,

                "created_at": plan.created_at

            })


        return Response(data)





class CPDActivityView(APIView):

    def get(self, request):

        activities = CPDActivity.objects.all()

        data = []


        for activity in activities:

            data.append({

                "id": activity.id,

                "plan": activity.plan.title,

                "teacher": activity.teacher,

                "activity": activity.activity,

                "date": activity.date,

                "status": activity.status

            })


        return Response(data)
