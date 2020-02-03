import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from vasso.config import DevelopmentConfig, ProductionConfig

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(config_class=DevelopmentConfig):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
        migrate.init_app(app, db)
        register_blueprints(app)

    return app


def register_blueprints(app):
    from vasso.auth import auth
    from vasso.accounts import accounts

    app.register_blueprint(auth)
    app.register_blueprint(accounts)
