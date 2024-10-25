from rest_framework import viewsets
from .models import Department, Fond, Category, Mtv, Format, Language, Region
from helper.serializers import (
    DepartmentSerializer, FondSerializer,
    CategorySerializer, MtvSerializer,
    FormatSerializer, LanguageSerializer,
    RegionSerializer
)
from authentication.permissions import IsGroupUserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsGroupUserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class FondViewSet(viewsets.ModelViewSet):
    queryset = Fond.objects.all()
    serializer_class = FondSerializer
    permission_classes = [IsGroupUserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsGroupUserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class MTVViewSet(viewsets.ModelViewSet):
    queryset = Mtv.objects.all()
    serializer_class = MtvSerializer
    permission_classes = [IsGroupUserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer
    permission_classes = [IsGroupUserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsGroupUserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsGroupUserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]
