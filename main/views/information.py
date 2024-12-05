from rest_framework import (
    viewsets, status, exceptions, filters, permissions, pagination,
    response, generics
)
from main.serializers import InformationSerializer, InformationCreateUpdateSerializer
from main.models import Information
from django_filters.rest_framework import DjangoFilterBackend
from utils.media import delete_media
from rest_framework_simplejwt.authentication import JWTAuthentication
from controller.permissions import IsOwnerPermission
from rest_framework.authentication import BasicAuthentication
from django.shortcuts import get_object_or_404


class InformationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsOwnerPermission]
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['region', 'language', 'year']
    search_fields = ['title', 'brief_data', 'summary', 'mtv_index', 'location_on_server']
    filterset_fields = [
        'fond__department__name',
        'category__parent__fond__department__name',
        'category__fond__name',
        'category__parent__name',
        'category__name',
        'region__name',
        'year',
        'month',
        'day',
        'is_serial'
    ]


class InformationCreateAPIView(generics.CreateAPIView):
    """
        Information creation API view
    """
    queryset = Information.objects.all()
    serializer_class = InformationCreateUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class InformationUpdateAPIView(generics.UpdateAPIView):
    """
        Update a model instance.
    """
    queryset = Information.objects.all()
    serializer_class = InformationCreateUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return response.Response(serializer.data)


class InformationDestroyAPIView(generics.DestroyAPIView):
    """
        Destroy a model instance.
    """
    serializer_class = InformationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(
            Information,
            pk=kwargs['pk']
        )
        self.perform_destroy(instance)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        if instance.poster is not None:
            name = instance.poster.image.name
            delete_media(name)
        cadre = instance.information.all()
        if cadre is not None:
            for item in cadre:
                delete_media(item.image.name)
        instance.delete()
