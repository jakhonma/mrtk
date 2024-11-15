from rest_framework import viewsets, generics, response, views
from .models import Department, Fond, Category, Mtv, Format, Language, Region
from helper.serializers import (
    DepartmentSerializer, FondSerializer,
    CategorySerializer, MtvSerializer,
    FormatSerializer, LanguageSerializer,
    RegionSerializer, NestedCategorySerializer,
    InformationCategorySerializer, HelperListSerializer
)
from authentication.permissions import IsGroupUserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class AbstractClassViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsGroupUserPermission, IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    pass


class DepartmentViewSet(AbstractClassViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class FondViewSet(AbstractClassViewSet):
    queryset = Fond.objects.all()
    serializer_class = FondSerializer


class FontListDepartmentAPIView(generics.ListAPIView):
    serializer_class = FondSerializer

    def get_queryset(self):
        queryset = Fond.objects.filter(
            department_id=self.kwargs['department_id']
        )
        return queryset


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


class CategoryFondListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Category.objects.filter(
            Q(fond_id=self.kwargs['fond_id']) |
            Q(parent__fond_id=self.kwargs['fond_id'])
        )
        return queryset

    serializer_class = InformationCategorySerializer


class HelperListView(generics.ListAPIView):
    """
        List a queryset.
        """

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
