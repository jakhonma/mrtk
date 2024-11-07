from rest_framework import serializers
from .models import Information, Poster, Cadre, Serial
from helper.serializers import FondSerializer, CategorySerializer


class InformationSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)

    class Meta:
        model = Information
        fields = '__all__'


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['pk', 'image']


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
