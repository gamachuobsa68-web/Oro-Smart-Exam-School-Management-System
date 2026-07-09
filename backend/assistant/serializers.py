from rest_framework import serializers


from .models import AssistantRequest





class AssistantRequestSerializer(serializers.ModelSerializer):


    user_name = serializers.CharField(

        source="user.username",

        read_only=True

    )


    class Meta:


        model = AssistantRequest


        fields = [

            "id",

            "user",

            "user_name",

            "request_type",

            "prompt",

            "response",

            "created_at",

        ]


        read_only_fields = [

            "id",

            "user",

            "response",

            "created_at",

        ]
