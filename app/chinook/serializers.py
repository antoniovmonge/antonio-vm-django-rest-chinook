from rest_framework import serializers

from chinook.models import Albums


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = "__all__"
        read_only_fields = ["album_id"]
