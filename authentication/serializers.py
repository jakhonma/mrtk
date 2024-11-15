from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.models import User, AdminUser, LeaderUser, EmployeeUser
from django.utils.translation import gettext_lazy as _


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token_class = RefreshToken

    default_error_messages = {
        "no_active_account": _("No active account found with the given credentials")
    }

    def validate(self, attrs):
        authenticate_kwargs = {
            "username": attrs["username"],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        user = authenticate(**authenticate_kwargs)

        if user is None:
            raise ValidationError("Username and Password error")

        refresh = self.get_token(user)

        attrs["refresh"] = str(refresh)
        attrs["access"] = str(refresh.access_token)

        del attrs["username"], attrs["password"]

        return attrs

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
