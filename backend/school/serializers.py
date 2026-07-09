from rest_framework import serializers

from .models import (

    School,

    AcademicYear,

    ClassRoom,

    Subject

)





# =========================
# SCHOOL SERIALIZER
# =========================

class SchoolSerializer(serializers.ModelSerializer):


    class Meta:

        model = School


        fields = [

            "id",

            "name",

            "address",

            "phone",

            "email",

            "logo",

            "created_at"

        ]


        read_only_fields = [

            "id",

            "created_at"

        ]






# =========================
# ACADEMIC YEAR SERIALIZER
# =========================

class AcademicYearSerializer(serializers.ModelSerializer):


    class Meta:

        model = AcademicYear


        fields = [

            "id",

            "name",

            "start_date",

            "end_date",

            "is_current"

        ]






# =========================
# CLASSROOM SERIALIZER
# =========================

class ClassRoomSerializer(serializers.ModelSerializer):


    class Meta:

        model = ClassRoom


        fields = [

            "id",

            "school",

            "name",

            "section",

            "academic_year",

            "capacity"

        ]






# =========================
# SUBJECT SERIALIZER
# =========================

class SubjectSerializer(serializers.ModelSerializer):


    class Meta:

        model = Subject


        fields = [

            "id",

            "name",

            "code",

            "description",

            "is_active"

        ]
