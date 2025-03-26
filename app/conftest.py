import os

from django.conf import settings

import pytest


DEFAULT_ENGINE = "django.db.backends.sqlite3"


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": DEFAULT_ENGINE,
        "NAME": ":memory:",
        "ATOMIC_REQUESTS": False,
    }
