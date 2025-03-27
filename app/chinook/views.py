from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Album, Artist
from .serializers import AlbumSerializer, ArtistSerializer, TrackSerializer


class AlbumList(APIView):
    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistList(APIView):
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetail(APIView):
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)


class ArtistAlbums(APIView):
    """
    Obtener todos los álbumes de un artista específico
    """

    def get_artist(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artist = self.get_artist(pk)
        albums = Album.objects.filter(artist_id=artist)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)


class AlbumTracks(APIView):
    """
    Obtener todas las pistas de un álbum específico
    """

    def get_album(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        album = self.get_album(pk)
        tracks = album.track_set.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
