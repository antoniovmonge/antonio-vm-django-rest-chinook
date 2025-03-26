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
