from rest_framework import serializers

from .models import StudentProfile



class StudentSerializer(serializers.ModelSerializer):


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


        model = StudentProfile


        fields = [

            "id",

            "user",

            "username",

            "first_name",

            "last_name",

            "student_id",

            "classroom",

            "photo",

            "parent_name",

            "parent_phone",

            "address",

            "date_of_birth",

            "gender",

            "is_active",

            "created_at",

            "updated_at",

        ]


        read_only_fields = [

            "id",

            "created_at",

            "updated_at",

        ]
