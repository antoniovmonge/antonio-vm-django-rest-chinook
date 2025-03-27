import pytest
from chinook.models import Artist


@pytest.mark.django_db
def test_artists_model():
    artist = Artist.objects.create(name="Artist Name")
    assert artist.name == "Artist Name"
