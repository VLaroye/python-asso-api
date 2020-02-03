import pytest

from vasso import create_app, db as _db
from vasso.config import TestingConfig


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    return app


@pytest.fixture
def db(app):
    _db.app = app
    _db.drop_all()
    _db.create_all()
    return _db





