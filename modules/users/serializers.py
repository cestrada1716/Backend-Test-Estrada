# import rest_framework modules
from rest_framework import serializers

# import constants and modules from this app
from .constants import USER_ROLES
from .models import UserCornershop


class CreateUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=200)
    slack_id = serializers.CharField(max_length=20)
    phone_number = serializers.CharField(max_length=10)
    user_type = serializers.ChoiceField(choices=USER_ROLES, required=False)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=500, required=True)

    class Meta:
        model = UserCornershop
        fields = (
            "id",
            "full_name",
            "slack_id",
            "phone_number",
            "user_type",
            "email",
            "password",
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=500, required=True)

    class Meta:
        model = UserCornershop
        fields = ("email", "password")
