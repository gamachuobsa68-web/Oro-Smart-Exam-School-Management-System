from rest_framework.views import APIView
from rest_framework.response import Response


from .models import (

    School,

    AcademicYear,

    ClassRoom,

    Subject

)


from .serializers import (

    SchoolSerializer,

    AcademicYearSerializer,

    ClassRoomSerializer,

    SubjectSerializer

)


from accounts.permissions import IsAdmin





# =========================
# SCHOOL LIST + CREATE
# =========================

class SchoolView(APIView):


    permission_classes = [

        IsAdmin

    ]


    def get(self, request):

        schools = School.objects.all()


        serializer = SchoolSerializer(

            schools,

            many=True

        )


        return Response(

            serializer.data

        )




    def post(self, request):

        serializer = SchoolSerializer(

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
# ACADEMIC YEAR
# =========================

class AcademicYearView(APIView):


    permission_classes = [

        IsAdmin

    ]


    def get(self, request):

        years = AcademicYear.objects.all()


        serializer = AcademicYearSerializer(

            years,

            many=True

        )


        return Response(

            serializer.data

        )




    def post(self, request):

        serializer = AcademicYearSerializer(

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
# CLASSROOM
# =========================

class ClassRoomView(APIView):


    permission_classes = [

        IsAdmin

    ]


    def get(self, request):

        classrooms = ClassRoom.objects.all()


        serializer = ClassRoomSerializer(

            classrooms,

            many=True

        )


        return Response(

            serializer.data

        )




    def post(self, request):

        serializer = ClassRoomSerializer(

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
# SUBJECT
# =========================

class SubjectView(APIView):


    permission_classes = [

        IsAdmin

    ]


    def get(self, request):

        subjects = Subject.objects.all()


        serializer = SubjectSerializer(

            subjects,

            many=True

        )


        return Response(

            serializer.data

        )




    def post(self, request):

        serializer = SubjectSerializer(

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
