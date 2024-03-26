import os


class Config:
    REDIS_HOST = os.environ["REDIS_HOST"]
    REDIS_PORT = os.environ["REDIS_PORT"]
    REDIS_DB = os.environ["REDIS_DB"]
    SALT: str = os.environ["SALT"]
    KEY_SIZE: int = int(os.environ.get("KEY_SIZE", 12))
    CODE_PHRASE_MIN_LENGTH: int = os.environ.get("CODE_PHRASE_MIN_LENGTH", 8)