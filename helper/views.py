from rest_framework import viewsets, generics, response, views
from .models import Department, Fond, Category, Mtv, Format, Language, Region
from helper.serializers import (
    DepartmentSerializer, FondSerializer,
    CategorySerializer, MtvSerializer,
    FormatSerializer, LanguageSerializer,
    RegionSerializer, NestedCategorySerializer,
    InformationCategorySerializer, HelperListSerializer
)
from controller.permissions import IsGroupUserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class AbstractClassViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsGroupUserPermission, IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    @method_decorator(cache_page(60 * 5))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


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
    

class FontListDepartmentAPIView(generics.ListAPIView):
    """
        Departmentga tegishli Fondlarni qaytaradigan View
    """
    serializer_class = FondSerializer

    def get_queryset(self):
        queryset = Fond.objects.filter(
            department_id=self.kwargs['department_id']
        )
        return queryset


class CategoryFondListView(generics.ListAPIView):
    """
        Fondga tegishli Categorylarni qaytaradigan View
    """
    def get_queryset(self):
        queryset = Category.objects.filter(
            fond_id=self.kwargs['fond_id'],
            fond__isnull=False
        )
        return queryset

    serializer_class = InformationCategorySerializer


class ParentCategoryListView(generics.ListAPIView):
    """
        Parentga tegishli Categorylarni qaytaradigan View
    """
    def get_queryset(self):
        queryset = Category.objects.filter(
            parent_id=self.kwargs['category_id'],
            fond__isnull=True
        )
        return queryset

    serializer_class = InformationCategorySerializer


class HelperListView(generics.ListAPIView):
    """
        Mtv, Region, Language va Format Listni qaytaradigan View 
    """
    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        mtvs = Mtv.objects.all()
        regions = Region.objects.all()
        languages = Language.objects.all()
        formats = Format.objects.all()

        data = {
            "mtvs": MtvSerializer(mtvs, many=True).data,
            "regions": RegionSerializer(regions, many=True).data,
            "languages": LanguageSerializer(languages, many=True).data,
            "formats": FormatSerializer(formats, many=True).data,
        }

        helpers = HelperListSerializer(data)

        return response.Response(helpers.data)
