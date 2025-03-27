import pytest
from chinook.serializers import AlbumSerializer


@pytest.mark.django_db
def test_valid_album_serializer():
    valid_serializer_data = {
        "title": "Album Title",
        "artist_id": 1,
    }
    serializer = AlbumSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data["title"] == valid_serializer_data["title"]
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_album_serializer():
    invalid_serializer_data = {
        "title": "Album Title",
    }
    serializer = AlbumSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.errors == {"artist_id": ["This field is required."]}
