from rest_framework import viewsets, status, views, exceptions, filters, permissions, pagination, response, parsers
from rest_framework.decorators import action
from .serializers import InformationSerializer, PosterSerializer, CadreSerializer, SerialSerializer
from .models import Information, Poster, Cadre, Serial
from django_filters.rest_framework import DjangoFilterBackend
from .utils import delete_media
# from .permissions import InformationPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from authentication.permissions import IsOwnerPermission
from rest_framework.authentication import BasicAuthentication


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwnerPermission]
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['region', 'language', 'date']
    search_fields = ['title', 'brief_data', 'summary', 'mtv_index', 'location_on_server']
    filterset_fields = ['category__name', 'region__name', 'date']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
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

    @action(methods=["POST"], detail=True, parser_classes=(parsers.MultiPartParser,), permission_classes=[])
    def poster(self, request, *args, **kwargs):
        serializer = PosterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        obj = self.get_object()
        obj.poster_id = serializer.data.get("pk")
        obj.save()
        return response.Response(data={"msg": "Ok"}, status=status.HTTP_201_CREATED)

    @action(methods=["DELETE"], detail=True, permission_classes=[])
    def delete_poster(self, request, *args, **kwargs):
        obj = self.get_object()
        pk = obj.poster.pk
        poster = Poster.objects.get(pk=pk)
        delete_media(poster.image.name)
        poster.delete()
        return response.Response(data={"msg": "Ok"}, status=status.HTTP_204_NO_CONTENT)


class CadreViewSet(viewsets.ModelViewSet):
    queryset = Cadre.objects.all()
    serializer_class = CadreSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)

    def create(self, request, *args, **kwargs):
        information_id = kwargs['information_id']
        serializer = self.get_serializer(data=request.data, context={'information_id': information_id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
            serial = Serial.objects.get(pk=pk)
            serial.delete()
            return response.Response(data={"msg": "Ok"}, status=status.HTTP_204_NO_CONTENT)
        except Serial.DoesNotExist:
            raise exceptions.ValidationError({"msg": "Serial with this id does not exist"})


class CadreAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        information_id = kwargs['information_id']
        if information_id is None:
            raise exceptions.ValidationError({'msg': 'No cadre was found in this information'})

        pk = kwargs.get('pk', None)
        if pk is not None:
            try:
                cadre = Cadre.objects.get(pk=pk)
                serializer = CadreSerializer(cadre)
                return response.Response(serializer.data)
            except Serial.DoesNotExist:
                raise exceptions.ValidationError({'msg': 'Cadre with this id does not exist'})

        cadre = Cadre.objects.all()
        serializer = CadreSerializer(cadre, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        information_id = kwargs['information_id']
        serializer = CadreSerializer(data=request.data, context={'information_id': information_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data={"msg": "Ok"}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            cadre = Cadre.objects.get(pk=pk)
            serializer = CadreSerializer(instance=cadre, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(data={"msg": "Ok"}, status=status.HTTP_200_OK)
        except Serial.DoesNotExist:
            raise exceptions.ValidationError({"msg": "Cadre with this id does not exist"})

    def delete(self, *args, **kwargs):
        pk = kwargs["pk"]

        try:
            cadre = Cadre.objects.get(pk=pk)
            delete_media(cadre.image.name)
            cadre.delete()
            return response.Response(data={"msg": "Ok"}, status=status.HTTP_204_NO_CONTENT)
        except Serial.DoesNotExist:
            raise exceptions.ValidationError({"msg": "Cadre with this id does not exist"})
