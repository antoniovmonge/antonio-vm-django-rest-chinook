import json

import pytest

from chinook.models import Artist, Album


@pytest.mark.django_db
def test_add_movie(client):
    artists = Artist.objects.all()
    assert len(artists) == 275

    resp = client.post(
        "/api/artists/",
        {
            "name": "The Big Band From Nowhere",
        },
        content_type="application/json",
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "The Big Band From Nowhere"

    artists = Artist.objects.all()
    assert len(artists) == 276


@pytest.mark.django_db
def test_get_single_movie(client):
    artist = Artist.objects.create(name="The Big Band From Nowhere")
    resp = client.get(f"/api/artists/{artist.artistid}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "The Big Band From Nowhere"


def test_get_single_artist_incorrect_id(client):
    resp = client.get("/api/artists/foo/")
    assert resp.status_code == 404
