from rest_framework.views import APIView
from rest_framework.response import Response


from .models import AssistantRequest


from .serializers import AssistantRequestSerializer


from rest_framework.permissions import IsAuthenticated



# =========================
# AI ASSISTANT REQUEST
# =========================

class AssistantView(APIView):

    permission_classes = [

        IsAuthenticated

    ]



    def get(self, request):

        requests = AssistantRequest.objects.filter(

            user=request.user

        )


        serializer = AssistantRequestSerializer(

            requests,

            many=True

        )


        return Response(

            serializer.data

        )




    def post(self, request):


        serializer = AssistantRequestSerializer(

            data=request.data

        )


        if serializer.is_valid():


            assistant_request = serializer.save(

                user=request.user

            )


            # Temporary assistant response
            # Booda AI model waliin wal qunnamsiisa

            if assistant_request.request_type == "QUESTION":

                assistant_request.response = (

                    "Question generation assistant ready."

                )


            elif assistant_request.request_type == "LESSON":

                assistant_request.response = (

                    "Lesson planning assistant ready."

                )


            elif assistant_request.request_type == "EXAM":

                assistant_request.response = (

                    "Exam preparation assistant ready."

                )


            assistant_request.save()



            return Response(

                AssistantRequestSerializer(

                    assistant_request

                ).data,

                status=201

            )


        return Response(

            serializer.errors,

            status=400

        )
