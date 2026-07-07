from rest_framework import serializers

from .models import (

    TeacherAssistant,

    LessonPlan,

    CPD,

    CPDReport

)



class TeacherAssistantSerializer(serializers.ModelSerializer):

    class Meta:

        model = TeacherAssistant

        fields = "__all__"





class LessonPlanSerializer(serializers.ModelSerializer):

    class Meta:

        model = LessonPlan

        fields = "__all__"





class CPDSerializer(serializers.ModelSerializer):

    class Meta:

        model = CPD

        fields = "__all__"





class CPDReportSerializer(serializers.ModelSerializer):

    class Meta:

        model = CPDReport

        fields = "__all__"
