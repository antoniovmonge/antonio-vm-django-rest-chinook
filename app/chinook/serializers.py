from rest_framework import serializers

from chinook.models import Album, Artist, Track


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
        read_only_fields = ["album_id"]


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
        read_only_fields = ["artist_id"]


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"
        read_only_fields = ["track_id"]


class AlbumSummarySerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source="artist_id.name")
    total_tracks = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ["album_id", "title", "artist_name", "total_tracks"]

    def get_total_tracks(self, obj):
        return obj.track_set.count()
