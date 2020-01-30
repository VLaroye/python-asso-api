import pytest
from tests.support.configure_test import app
from vasso.config import (
    get_env_db_url,
    TestingConfig,
    DevelopmentConfig,
    ProductionConfig,
)


def test_development_config(app):
    test_app = app(DevelopmentConfig)
    db_url = get_env_db_url('development')

    assert test_app.config['DEBUG']
    assert not test_app.config['TESTING']
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == db_url


def test_testing_config(app):
    test_app = app(TestingConfig)
    db_url = get_env_db_url('testing')

    assert test_app.config['DEBUG']
    assert test_app.config['TESTING']
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == db_url


def test_production_config(app):
    test_app = app(ProductionConfig)
    db_url = get_env_db_url('production')

    assert not test_app.config['DEBUG']
    assert not test_app.config['TESTING']
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == db_url
