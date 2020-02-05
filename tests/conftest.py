import pytest

from vasso import create_app, db as _db
from vasso.config import TestingConfig

from vasso.auth.models import User
from vasso.accounts.models import Account


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    return app


@pytest.fixture
def db(app):
    _db.app = app
    _db.drop_all()
    _db.create_all()

    # Insert fake data
    user1 = User(username="User1", email="user1@email.com")
    account1 = Account(name='Account 1', owner_id='1')

    _db.session.add(user1)
    _db.session.add(account1)
    _db.session.commit()

    return _db
