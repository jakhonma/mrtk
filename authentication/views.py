from rest_framework import viewsets, generics, response, status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from authentication.models import User
from authentication.serializers import UserSerializer, LoginSerializer


class LoginAPIView(generics.GenericAPIView):
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_serializer_class(self):
        serializer = LoginSerializer
        return serializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return response.Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        return queryset

    def get_serializer_class(self):
        return UserSerializer
