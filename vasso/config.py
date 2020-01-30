from vasso.utils.get_env_variable import get_env_variable


def create_db_url(user, password, host, port, db_name):
    return f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'


# TODO: Unify these ENV variables by pulling from different dot files
def get_env_db_url(env_setting):
    if env_setting == "testing":
        db_user = get_env_variable("TESTING_DB_USER")
        db_password = get_env_variable("TESTING_DB_PASSWORD")
        db_host = get_env_variable("TESTING_DB_HOST")
        db_port = get_env_variable("TESTING_DB_PORT")
        db_name = get_env_variable("TESTING_DB_NAME")
    elif env_setting == "production":
        db_user = get_env_variable("PRODUCTION_DB_USER")
        db_password = get_env_variable("PRODUCTION_DB_PASSWORD")
        db_host = get_env_variable("PRODUCTION_DB_HOST")
        db_port = get_env_variable("PRODUCTION_DB_PORT")
        db_name = get_env_variable("PRODUCTION_DB_NAME")
    else:
        db_user = get_env_variable("DEVELOPMENT_DB_USER")
        db_password = get_env_variable("DEVELOPMENT_DB_PASSWORD")
        db_host = get_env_variable("DEVELOPMENT_DB_HOST")
        db_port = get_env_variable("DEVELOPMENT_DB_PORT")
        db_name = get_env_variable("DEVELOPMENT_DB_NAME")

    return create_db_url(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        db_name=db_name,
    )


# DB URLS for each Environment
DEV_DB_URL = get_env_db_url('development')
TESTING_DB_URL = get_env_db_url('testing')
PRODUCTION_DB_URL = get_env_db_url('production')


class Config:
    # SQL Alchemy settings
    SQLALCHEMY_DATABASE_URI = DEV_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask settings
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = TESTING_DB_URL
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = PRODUCTION_DB_URL
