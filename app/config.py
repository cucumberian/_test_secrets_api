import os


class Config:
    REDIS_HOST = os.environ["REDIS_HOST"]
    REDIS_PORT = os.environ["REDIS_PORT"]
    REDIS_DB = os.environ["REDIS_DB"]
    SALT: str = os.environ["SALT"]
