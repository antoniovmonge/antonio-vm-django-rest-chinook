from django.contrib import admin

from chinook.models import Album, Artist


@admin.register(Album)
class AlbumsAdmin(admin.ModelAdmin):
    fields = ("album_id", "title", "artist_id")
    list_display = ("album_id", "title", "artist_id")


@admin.register(Artist)
class ArtistsAdmin(admin.ModelAdmin):
    fields = ("artist_id", "name")
    list_display = ("artist_id", "name")
