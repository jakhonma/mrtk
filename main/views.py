from rest_framework import (
    viewsets, status, views, exceptions, filters, permissions, pagination,
    response, parsers, generics,
)
from rest_framework.exceptions import ValidationError
from .serializers import (
    InformationSerializer, PosterSerializer,
    CadreSerializer, SerialSerializer, InformationCreateUpdateSerializer
)
from .models import Information, Poster, Cadre, Serial
from django_filters.rest_framework import DjangoFilterBackend
from .utils import delete_media
from rest_framework_simplejwt.authentication import JWTAuthentication
from authentication.permissions import IsOwnerPermission
from rest_framework.authentication import BasicAuthentication
from django.db import transaction
from django.shortcuts import get_object_or_404


class InformationViewSet(viewsets.ModelViewSet):
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
        'day'
    ]

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return response.Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def perform_destroy(self, instance):
    #     if instance.poster is not None:
    #         name = instance.poster.image.name
    #         delete_media(name)
    #     cadre = instance.information.all()
    #     if cadre is not None:
    #         for item in cadre:
    #             delete_media(item.image.name)
    #     instance.delete()


class InformationCreateAPIView(generics.CreateAPIView):
    """Information creation API view"""
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

    def perform_create(self, serializer):
        serializer.save()


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

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


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


class PosterCreateAPIView(generics.CreateAPIView):
    """Viewda ma'lum informisionga poster qo'shadi"""
    # parser_classes = (parsers.MultiPartParser,)
    permission_classes = []

    def create(self, request, *args, **kwargs):
        """Create a poster."""
        information_id = kwargs['information_id']
        serializer = PosterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Information,
                    id=information_id
                )
                obj.poster_id = serializer.data.get("pk")
                obj.save()
                return response.Response(
                    data={"msg": "Ok", "data": serializer.data},
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            raise ValidationError({"msg": f"Transaction failed: {e}"})


class PosterDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

    def destroy(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            with transaction.atomic():
                instance = get_object_or_404(
                    Poster,
                    pk=pk
                )
                delete_media(instance.image.name)
                instance.delete()
                return response.Response(
                    data={"msg": "Ok"},
                    status=status.HTTP_204_NO_CONTENT
                )
        except Exception as e:
            raise ValidationError({"msg": f"Transaction failed: {e}"})


# Kadrlar uchun views
class CadreListAPIView(generics.ListAPIView):
    """
        Cadrelar Listini qaytaradi
    """
    # queryset = Cadre.objects.all()
    serializer_class = CadreSerializer

    def get_queryset(self):
        queryset = Cadre.objects.filter(information_id=self.kwargs['information_id'])
        return queryset


class CadreCreateAPIView(generics.CreateAPIView):
    serializer_class = CadreSerializer
    parser_classes = (parsers.MultiPartParser,)

    def create(self, request, *args, **kwargs):
        information_id = kwargs['information_id']
        serializer = self.get_serializer(
            data=request.data,
            context={'information_id': information_id}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class CadreDeleteAPIView(generics.DestroyAPIView):
    """
        Destroy a model instance.
    """
    queryset = Cadre.objects.all()
    serializer_class = CadreSerializer

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Cadre, pk=self.kwargs['pk'])
        delete_media(instance.image.name)
        self.perform_destroy(instance)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class SerialAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        information_id = kwargs['information_id']
        if information_id is None:
            raise exceptions.ValidationError({'msg': 'No series was found in this information'})

        pk = kwargs.get('pk', None)
        if pk is not None:
            try:
                serial = Serial.objects.get(pk=pk)
                serializer = SerialSerializer(serial)
                return response.Response(serializer.data)
            except Serial.DoesNotExist:
                raise exceptions.ValidationError({'msg': 'Serial with this id does not exist'})

        serial = Serial.objects.all()
        serializer = SerialSerializer(serial, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        information_id = kwargs['information_id']
        serializer = SerialSerializer(data=request.data, context={'information_id': information_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data={"msg": "Ok"}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            serial = Serial.objects.get(pk=pk)
            serializer = SerialSerializer(instance=serial, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(data={"msg": "Ok"}, status=status.HTTP_200_OK)
        except Serial.DoesNotExist:
            raise exceptions.ValidationError({"msg": "Serial with this id does not exist"})

    def delete(self, *args, **kwargs):
        pk = kwargs["pk"]
        try:
            with transaction.atomic():
                serial = Serial.objects.get(pk=pk)
                serial.delete()
                return response.Response(data={"msg": "Ok"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise ValidationError({"msg": f"Transaction failed: {e}"})


# class CadreAPIView(views.APIView):
#     def get(self, request, *args, **kwargs):
#         information_id = kwargs['information_id']
#         if information_id is None:
#             raise exceptions.ValidationError({'msg': 'No cadre was found in this information'})
#
#         pk = kwargs.get('pk', None)
#         if pk is not None:
#             try:
#                 cadre = get_object_or_404(Cadre, pk=pk, information_id=information_id)
#                 serializer = CadreSerializer(cadre)
#                 return response.Response(serializer.data)
#             except Serial.DoesNotExist:
#                 raise exceptions.ValidationError({'msg': 'Cadre with this id does not exist'})
#
#         cadre = Cadre.objects.all()
#         serializer = CadreSerializer(cadre, many=True)
#         return response.Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         information_id = kwargs['information_id']
#         serializer = CadreSerializer(data=request.data, context={'information_id': information_id})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return response.Response(data={"msg": "Ok"}, status=status.HTTP_201_CREATED)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs['pk']
#         try:
#             cadre = Cadre.objects.get(pk=pk)
#             serializer = CadreSerializer(instance=cadre, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return response.Response(data={"msg": "Ok"}, status=status.HTTP_200_OK)
#         except Serial.DoesNotExist:
#             raise exceptions.ValidationError({"msg": "Cadre with this id does not exist"})
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs["pk"]
#         try:
#             with transaction.atomic():
#                 cadre = Cadre.objects.get(pk=pk)
#                 delete_media(cadre.image.name)
#                 cadre.delete()
#                 return response.Response(data={"msg": "Ok"}, status=status.HTTP_204_NO_CONTENT)
#         except Exception as e:
#             raise ValidationError({"msg": f"Transaction failed: {e}"})
