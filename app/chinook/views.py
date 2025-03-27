from django.http import Http404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Album, Artist
from .serializers import (
    AlbumSerializer,
    AlbumSummarySerializer,
    ArtistSerializer,
    TrackSerializer,
)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 100


class AlbumList(ListAPIView):
    """
    Obtener todos los discos
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = StandardResultsSetPagination


# class AlbumList(APIView):
#     def get(self, request, format=None):
#         albums = Album.objects.all()
#         serializer = AlbumSerializer(albums, many=True)
#         return Response(serializer.data)


class ArtistList(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        artists = Artist.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(artists, request)
        serializer = ArtistSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

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


class AlbumSummaryList(APIView):
    """
    Obtener todos los álbumes, incluyendo el nombre del artista y el número total tracks
    """

    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        albums = Album.objects.all().select_related("artist_id")
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(albums, request)
        serializer = AlbumSummarySerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
