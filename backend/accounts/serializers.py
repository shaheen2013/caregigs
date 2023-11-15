from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            "is_superuser",
            "is_staff",
            "is_active",
            # "date_joined",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
        read_only_fields = [
            "last_login",
        ]
