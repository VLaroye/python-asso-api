import pytest

from vasso import create_app, db
from vasso.config import get_env_db_url, TestingConfig


@pytest.yield_fixture()
def app():
    def _app(config_class):
        test_app = create_app(config_class)
        test_app.test_request_context().push()

        if config_class is TestingConfig:
            # Starts with and empty db
            db.drop_all()

            from vasso.accounts.models import Account
            from vasso.auth.models import User

            db.create_all()

        return test_app

    yield _app
    db.session.remove()

    if str(db.engine.url) == TestingConfig.SQLALCHEMY_DATABASE_URI:
        db.drop_all()
