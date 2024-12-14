from rest_framework import serializers
from django.contrib.auth.models import Group, Permission, ContentType


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'


# class ContentTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContentType
#         fields = '__all__'
