import pytest
from chinook.models import Albums, Artists


# @pytest.mark.django_db
# def test_albums_model():
#     album = Albums.objects.create(title="Album Title", artistid=1)
#     assert album.album_id == 1
#     assert album.title == "Album Title"
#     assert album.artistid == 1


@pytest.mark.django_db
def test_artists_model():
    artist = Artists.objects.create(name="Artist Name")
    # assert artist.artistid == 1
    assert artist.name == "Artist Name"
