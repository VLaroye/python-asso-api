import os


def get_env_variable(name):
    try:
        return os.environ.get(name)
    except KeyError:
        message = f"Expected env variable {name} not set"
        raise Exception(message)
