from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from .utils import add_many_to_many, edit_many_to_many
from helper.models import Mtv, Region, Language, Format
from .models import Information, Poster, Cadre, Serial
from helper.serializers import (
    FondSerializer, NestedCategorySerializer,
    CategorySerializer, MtvSerializer, RegionSerializer,
    LanguageSerializer, FormatSerializer, InformationCategorySerializer
)


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['pk', 'image']


class InformationSerializer(serializers.ModelSerializer):
    fond = FondSerializer(required=True)
    category = InformationCategorySerializer(required=False)
    mtv = MtvSerializer(many=True, required=False)
    region = RegionSerializer(many=True, required=False)
    language = LanguageSerializer(many=True, required=False)
    format = FormatSerializer(many=True, required=False)
    poster = PosterSerializer(required=False)

    class Meta:
        model = Information
        fields = '__all__'


class InformationCreateUpdateSerializer(serializers.Serializer):
    COLOURED = 'coloured'
    WRITE_BLACK = 'write_black'
    COLORS = (
        (COLOURED, 'coloured'),
        (WRITE_BLACK, 'white-black')
    )

    ETHER = 'ether'
    PRIMARY = 'primary'
    MATERIAL = (
        (ETHER, 'ether'),
        (PRIMARY, 'primary')
    )

    fond_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    mtv = serializers.PrimaryKeyRelatedField(queryset=Mtv.objects.all(), many=True, required=False)
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), many=True, required=False)
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True, required=False)
    format = serializers.PrimaryKeyRelatedField(queryset=Format.objects.all(), many=True, required=False)
    title = serializers.CharField(max_length=255)
    mtv_index = serializers.CharField(max_length=100)
    location_on_server = serializers.CharField(max_length=250)
    color = serializers.ChoiceField(choices=COLORS, default=COLOURED)
    material = serializers.ChoiceField(choices=MATERIAL, default=ETHER)
    duration = serializers.TimeField(required=False)
    year = serializers.IntegerField(validators=[
        MinValueValidator(1920, message="Yilni tug'ri kiriting?"),
        MaxValueValidator(int(date.today().year), message="Yilni tug'ri kiriting?")
    ])
    month = serializers.IntegerField(validators=[
        MinValueValidator(1, message="Oyni tug'ri kiriting?"),
        MaxValueValidator(12, message="Oyni tug'ri kiriting?")
    ], required=False)
    day = serializers.IntegerField(validators=[
        MinValueValidator(1, message="Kunni tug'ri kiriting?"),
        MaxValueValidator(31, message="Kunni tug'ri kiriting?")
    ], required=False)
    single_code = serializers.IntegerField(read_only=True)
    restoration = serializers.BooleanField(default=False)
    confidential = serializers.BooleanField(default=False)
    brief_data = serializers.CharField(max_length=500)
    summary = serializers.CharField(max_length=500)
    is_serial = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        mtvs = validated_data.pop('mtv')
        regions = validated_data.pop('region')
        languages = validated_data.pop('language')
        formats = validated_data.pop('format')

        # employee = self.context['request'].user
        # information = Information.objects.create(employee=employee, **validated_data)

        information = Information.objects.create(**validated_data)
        add_many_to_many(information.mtv, mtvs)
        add_many_to_many(information.region, regions)
        add_many_to_many(information.language, languages)
        add_many_to_many(information.format, formats)

        return information

    def update(self, instance, validated_data):
        mtvs = validated_data.pop('mtv')
        regions = validated_data.pop('region')
        languages = validated_data.pop('language')
        formats = validated_data.pop('format')

        # employee = self.context['request'].user
        #
        # # Postni o'zgartirish huquqini tekshirish
        # if instance.employee != employee:
        #     raise PermissionDenied("Siz faqat o'zingizning postlaringizni yangilashingiz mumkin.")

        instance.fond_id = validated_data.get('fond_id', instance.fond.id)
        instance.category_id = validated_data.get('category_id', instance.category.id)
        instance.mtv_index = validated_data.get('mtv_index', instance.mtv_index)
        instance.location_on_server = validated_data.get('location_on_server', instance.location_on_server)
        instance.color = validated_data.get('color', instance.color)
        instance.material = validated_data.get('material', instance.material)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.year = validated_data.get('year', instance.year)
        instance.month = validated_data.get('month', instance.month)
        instance.day = validated_data.get('day', instance.day)
        instance.restoration = validated_data.get('restoration', instance.restoration)
        instance.confidential = validated_data.get('confidential', instance.confidential)
        instance.brief_data = validated_data.get('brief_data', instance.brief_data)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.is_serial = validated_data.get('is_serial', instance.is_serial)
        instance.save()

        edit_many_to_many(instance.mtv, mtvs)
        edit_many_to_many(instance.region, regions)
        edit_many_to_many(instance.language, languages)
        edit_many_to_many(instance.format, formats)

        return instance


class CadreSerializer(serializers.Serializer):
    image = serializers.ImageField()
    information_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        validated_data['information_id'] = self.context['information_id']
        return Cadre.objects.create(**validated_data)


class SerialSerializer(serializers.Serializer):
    information_id = serializers.IntegerField(required=False)
    part = serializers.IntegerField(required=False)
    duration = serializers.TimeField()

    def create(self, validated_data):
        validated_data['information_id'] = self.context['information_id']
        return Serial.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.part = validated_data.get('part', instance.part)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
