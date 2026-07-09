from rest_framework import serializers

from .models import (
    CPDPlan,
    CPDActivity
)


class CPDPlanSerializer(serializers.ModelSerializer):

    class Meta:

        model = CPDPlan

        fields = "__all__"


class CPDActivitySerializer(serializers.ModelSerializer):

    teacher_name = serializers.CharField(
        source="teacher.username",
        read_only=True
    )

    class Meta:

        model = CPDActivity

        fields = "__all__"
