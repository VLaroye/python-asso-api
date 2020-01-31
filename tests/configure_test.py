import pytest

from vasso import create_app, db
from vasso.config import TestingConfig

from vasso.auth.models import User
from vasso.accounts.models import Account


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(TestingConfig)

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    # Insert some data, if needed
    user1 = User(username='user7', email='user7@email.com')
    account1 = Account(name='account7', created_by='1')

    db.session.add(user1)
    db.session.add(account1)

    # Commit the db changes
    db.session.commit()

    yield db

    db.drop_all()
