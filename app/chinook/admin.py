from django.contrib import admin

from chinook.models import Album, Artist


@admin.register(Album)
class AlbumsAdmin(admin.ModelAdmin):
    fields = ("album_id", "title", "artistid")
    list_display = ("album_id", "title", "artistid")


@admin.register(Artist)
class ArtistsAdmin(admin.ModelAdmin):
    fields = ("artistid", "name")
    list_display = ("artistid", "name")
