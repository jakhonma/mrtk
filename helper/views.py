from rest_framework import viewsets, generics
from .models import Department, Fond, Category, Mtv, Format, Language, Region
from helper.serializers import (
    DepartmentSerializer, FondSerializer,
    CategorySerializer, MtvSerializer,
    FormatSerializer, LanguageSerializer,
    RegionSerializer, NestedCategorySerializer
)
from authentication.permissions import IsGroupUserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class AbstractClassViewSet(viewsets.ModelViewSet):
    permission_classes = [IsGroupUserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class DepartmentViewSet(AbstractClassViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class FondViewSet(AbstractClassViewSet):
    queryset = Fond.objects.all()
    serializer_class = FondSerializer


class MTVViewSet(AbstractClassViewSet):
    queryset = Mtv.objects.all()
    serializer_class = MtvSerializer


class FormatViewSet(AbstractClassViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class LanguageViewSet(AbstractClassViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class RegionViewSet(AbstractClassViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(fond__isnull=False)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = NestedCategorySerializer
