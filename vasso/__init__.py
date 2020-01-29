import os
from flask import Flask
from dotenv import load_dotenv


def create_app(test_config=None):
    load_dotenv()

    # Compute database uri
    db_user = os.environ.get('DB_USER', '')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', 5432)
    db_name = os.environ.get('DB_NAME', '')

    db_uri = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=db_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        # Load the instance config, if it exits, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config, if passed in
        app.config.from_mapping(test_config)

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from vasso.models import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/hello')
    def hello():
        return 'Hello, world !'

    return app
