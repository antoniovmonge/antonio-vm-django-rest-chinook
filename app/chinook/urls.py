from django.urls import path

from .views import (
    AlbumList,
    ArtistList,
    ArtistDetail,
    ArtistAlbums,
    AlbumTracks,
    AlbumSummaryList,
)


urlpatterns = [
    path("albums/", AlbumList.as_view()),
    path("artists/", ArtistList.as_view()),
    path("artists/<int:pk>/", ArtistDetail.as_view()),
    path("artists/<int:pk>/albums/", ArtistAlbums.as_view(), name="artist-albums"),
    path("albums/<int:pk>/tracks/", AlbumTracks.as_view(), name="album-tracks"),
    path("albums/summary/", AlbumSummaryList.as_view(), name="album-summary"),
]
