from rest_framework import viewsets
from authentication.models import User
from authentication.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        return queryset

    def get_serializer_class(self):
        return UserSerializer
