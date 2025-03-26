from django.urls import path

from .views import AlbumList, ArtistList


urlpatterns = [
    path("api/albums/", AlbumList.as_view()),
    path("api/artists/", ArtistList.as_view()),
]
