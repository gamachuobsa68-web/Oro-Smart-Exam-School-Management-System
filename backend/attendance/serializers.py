from rest_framework import serializers


from .models import Attendance





class AttendanceSerializer(serializers.ModelSerializer):


    student_name = serializers.CharField(

        source="student.username",

        read_only=True

    )


    marked_by_name = serializers.CharField(

        source="marked_by.username",

        read_only=True

    )


    class Meta:


        model = Attendance


        fields = [

            "id",

            "student",

            "student_name",

            "classroom",

            "date",

            "status",

            "marked_by",

            "marked_by_name",

            "created_at",

        ]


        read_only_fields = [

            "id",

            "date",

            "created_at",

        ]
