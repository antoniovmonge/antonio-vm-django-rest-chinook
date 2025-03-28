import pytest

from chinook.models import Artist


@pytest.mark.django_db
def test_get_artist_albums(client, add_artist, add_album):
    created_artist = add_artist(name="The Big Band From Nowhere")
    artist = Artist.objects.get(artist_id=created_artist.artist_id)
    album = add_album(
        title="The Test Album",
        artist=artist,
    )
    resp = client.get(f"/api/v1/artists/{artist.artist_id}/albums/")
    assert resp.status_code == 200
    assert resp.data[0]["title"] == "The Test Album"
    assert resp.data[0]["artist_id"] == artist.artist_id
    assert resp.data[0]["album_id"] == album.album_id


@pytest.mark.django_db
def test_get_artist_albums_incorrect_id(client):
    resp = client.get("/api/v1/artists/bad/albums/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_artists(client, add_artist):
    resp = client.get("/api/v1/artists/")
    assert resp.status_code == 200
