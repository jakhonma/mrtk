from .models import Department, Fond, Category, Mtv, Format, Language, Region
from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError


class AbstractClassSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance


class DepartmentSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     return Department.objects.create(**validated_data)
    class Meta:
        model = Department
        fields = '__all__'


class FondSerializer(serializers.Serializer):
    department = DepartmentSerializer()
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Fond.objects.create(**validated_data)


class MtvSerializer(AbstractClassSerializer):
    def create(self, validated_data):
        return Mtv.objects.create(**validated_data)


class FormatSerializer(AbstractClassSerializer):
    def create(self, validated_data):
        return Format.objects.create(**validated_data)


class RegionSerializer(AbstractClassSerializer):
    def create(self, validated_data):
        return Region.objects.create(**validated_data)


class LanguageSerializer(AbstractClassSerializer):
    def create(self, validated_data):
        return Language.objects.create(**validated_data)


class NestedCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'fond', 'parent']

    def validate(self, attrs):
        category = Category(**attrs)
        try:
            category.clean()
        except DjangoValidationError as e:
            raise DRFValidationError({"msg": e.message})
        return attrs


class InformationCategorySerializer(serializers.ModelSerializer):

    parent = NestedCategorySerializer(required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'fond', 'parent']


class CategorySerializer(serializers.ModelSerializer):
    children = NestedCategorySerializer(many=True, read_only=True)
    fond = FondSerializer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'fond', 'children']
