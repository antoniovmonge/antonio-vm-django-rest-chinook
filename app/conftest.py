import pytest
from chinook.models import Artist, Album
from django.conf import settings

DEFAULT_ENGINE = "django.db.backends.sqlite3"


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": DEFAULT_ENGINE,
        "NAME": ":memory:",
        "ATOMIC_REQUESTS": False,
    }


@pytest.fixture(scope="function")
def add_artist():
    def _add_artist(name):
        artist = Artist.objects.create(name=name)
        return artist

    return _add_artist


@pytest.fixture(scope="function")
def add_album():
    def _add_album(title, artist):
        album = Album.objects.create(
            title=title,
            artist_id=artist,
        )
        return album

    return _add_album
