from rest_framework import serializers

from chinook.models import Album, Artist


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
        read_only_fields = ["album_id"]


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
        read_only_fields = ["artistid"]
