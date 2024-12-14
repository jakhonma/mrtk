from rest_framework import serializers
from main.models import Bookmark
from main.serializers.information import InformationSerializer


class BookmarkListSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    information = InformationSerializer()


class BookmarkSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    information_id = serializers.IntegerField()

    def create(self, validated_data):
        bookmark = Bookmark.objects.create(
            user_id=self.context["user_id"],
            **validated_data
        )
        return bookmark
