from rest_framework import serializers

from .models import ReportCard



class ReportCardSerializer(serializers.ModelSerializer):

    class Meta:

        model = ReportCard

        fields = [
            "id",
            "student",
            "academic_year",
            "total_mark",
            "average",
            "rank",
            "grade",
            "status",
            "teacher_comment",
            "principal_comment",
            "created_at",
        ]
