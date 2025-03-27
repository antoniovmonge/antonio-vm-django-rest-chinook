from django.urls import path

from .views import AlbumList, ArtistList, ArtistDetail, ArtistAlbums, AlbumTracks


urlpatterns = [
    path("api/albums/", AlbumList.as_view()),
    path("api/artists/", ArtistList.as_view()),
    path("api/artists/<int:pk>/", ArtistDetail.as_view()),
    path("api/artists/<int:pk>/albums/", ArtistAlbums.as_view(), name="artist-albums"),
    path("api/albums/<int:pk>/tracks/", AlbumTracks.as_view(), name="album-tracks"),
]
