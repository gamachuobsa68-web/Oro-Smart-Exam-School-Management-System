from rest_framework import serializers

from .models import User



# =========================
# USER VIEW SERIALIZER
# =========================

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [

            "id",

            "username",

            "email",

            "first_name",

            "last_name",

            "role",

            "phone",

            "profile_image",

            "school_name",

            "address",

            "date_of_birth",

            "is_verified",

            "created_at",

        ]


        read_only_fields = [

            "id",

            "is_verified",

            "created_at",

        ]





# =========================
# USER REGISTRATION
# =========================

class RegisterSerializer(serializers.ModelSerializer):


    password = serializers.CharField(

        write_only=True,

        min_length=6

    )


    class Meta:

        model = User


        fields = [

            "username",

            "email",

            "password",

            "first_name",

            "last_name",

            "role",

            "phone",

        ]



    def create(self, validated_data):


        user = User.objects.create_user(

            username=validated_data["username"],

            email=validated_data.get("email"),

            password=validated_data["password"],

            first_name=validated_data.get(
                "first_name",
                ""
            ),

            last_name=validated_data.get(
                "last_name",
                ""
            ),

            role=validated_data.get(
                "role",
                "STUDENT"
            ),

            phone=validated_data.get(
                "phone"
            )

        )


        return user
