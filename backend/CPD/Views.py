from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CPDPlan


class CPDListView(APIView):

    def get(self, request):
        data = CPDPlan.objects.all()

        result = []

        for item in data:
            result.append({
                "title": item.title,
                "description": item.description,
                "month": item.month
            })

        return Response(result)
