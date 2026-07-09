from rest_framework import serializers


from .models import (

    TeacherAssistant,

    LessonPlan,

    CPD,

    CPDReport

)





# =========================
# TEACHER ASSISTANT
# =========================

class TeacherAssistantSerializer(serializers.ModelSerializer):


    teacher_name = serializers.CharField(

        source="teacher.username",

        read_only=True

    )


    class Meta:


        model = TeacherAssistant


        fields = [

            "id",

            "teacher",

            "teacher_name",

            "qualification",

            "specialization",

            "phone",

            "created_at",

        ]


        read_only_fields = [

            "id",

            "created_at",

        ]







# =========================
# LESSON PLAN
# =========================

class LessonPlanSerializer(serializers.ModelSerializer):


    teacher_name = serializers.CharField(

        source="teacher.username",

        read_only=True

    )


    class Meta:


        model = LessonPlan


        fields = [

            "id",

            "teacher",

            "teacher_name",

            "subject",

            "classroom",

            "topic",

            "objective",

            "teaching_method",

            "learning_activity",

            "assessment",

            "date",

            "created_at",

        ]


        read_only_fields = [

            "id",

            "created_at",

        ]







# =========================
# CPD
# =========================

class CPDSerializer(serializers.ModelSerializer):


    teacher_name = serializers.CharField(

        source="teacher.username",

        read_only=True

    )


    class Meta:


        model = CPD


        fields = [

            "id",

            "teacher",

            "teacher_name",

            "title",

            "description",

            "month",

            "hours",

            "status",

            "created_at",

        ]


        read_only_fields = [

            "id",

            "created_at",

        ]







# =========================
# CPD REPORT
# =========================

class CPDReportSerializer(serializers.ModelSerializer):


    teacher_name = serializers.CharField(

        source="teacher.username",

        read_only=True

    )


    class Meta:


        model = CPDReport


        fields = [

            "id",

            "teacher",

            "teacher_name",

            "month",

            "completed_cpd",

            "total_hours",

            "comment",

            "created_at",

        ]


        read_only_fields = [

            "id",

            "created_at",

    ]
