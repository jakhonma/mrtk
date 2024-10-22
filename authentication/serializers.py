from rest_framework import serializers
from authentication.models import User, AdminUser, LeaderUser, EmployeeUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                    "write_only": True,
                },
            'date_joined': {
                "write_only": True,
            }
        }
