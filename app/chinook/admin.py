from django.contrib import admin

from chinook.models import Albums, Artists


@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    fields = ("album_id", "title", "artistid")
    list_display = ("album_id", "title", "artistid")
