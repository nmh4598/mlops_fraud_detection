from os import getenv


def db_uri() -> str:
    return "{}://{}:{}@{}/{}".format(
        getenv("DB_TYPE"),
        getenv("DB_USER"),
        getenv("DB_PASSWORD"),
        getenv("DB_HOST"),
        getenv("DB_NAME"),
    )
