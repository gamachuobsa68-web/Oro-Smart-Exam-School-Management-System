from rest_framework import serializers

from .models import ReportCard



class ReportCardSerializer(serializers.ModelSerializer):


    student_username = serializers.CharField(

        source="student.username",

        read_only=True

    )


    class Meta:


        model = ReportCard


        fields = [

            "id",

            "student",

            "student_username",

            "academic_year",

            "total_mark",

            "average",

            "rank",

            "grade",

            "status",

            "teacher_comment",

            "principal_comment",

            "created_at",

            "updated_at",

        ]


        read_only_fields = [

            "id",

            "grade",

            "status",

            "created_at",

            "updated_at",

        ]
