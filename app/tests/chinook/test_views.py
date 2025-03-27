import pytest


@pytest.mark.django_db
def test_get_single_artist(client, add_artist):
    artist = add_artist(name="The Big Band From Nowhere")
    resp = client.get(f"/api/v1/artists/{artist.artist_id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "The Big Band From Nowhere"


@pytest.mark.django_db
def test_get_single_artist_incorrect_id(client):
    resp = client.get("/api/v1/artists/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_artists(client, add_artist):
    resp = client.get("/api/v1/artists/")
    assert resp.status_code == 200
