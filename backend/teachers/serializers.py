from rest_framework import serializers

from .models import Teacher



class TeacherSerializer(serializers.ModelSerializer):


    username = serializers.CharField(
        source="user.username",
        read_only=True
    )


    first_name = serializers.CharField(
        source="user.first_name",
        read_only=True
    )


    last_name = serializers.CharField(
        source="user.last_name",
        read_only=True
    )


    class Meta:

        model = Teacher


        fields = [

            "id",

            "user",

            "username",

            "first_name",

            "last_name",

            "employee_id",

            "subjects",

            "classrooms",

            "phone",

            "qualification",

            "experience_years",

            "is_active",

            "created_at",

        ]


        read_only_fields = [

            "id",

            "created_at",

        ]
