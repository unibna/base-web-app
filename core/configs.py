from enum import Enum

class Environments(Enum):
    LOCAL: str = "local"
    STAGING: str = "staging"
    PRODUCTION: str = "production"


class RedisConfig:
    HOST: str = ""
    PORT: int = 0 
    USERNAME: str = ""
    PASSWORD: str = ""

    def __init__(self, *args, **kwargs):
        self.HOST = kwargs.get("address", "")
        self.PORT = kwargs.get("port", 0)
        self.USERNAME = kwargs.get("username", "")
        self.PASSWORD = kwargs.get("password", "")

class Settings:
    ENVIRONMENT: str = Environments.LOCAL

    REDIS = RedisConfig(
        address="localhost",
        port=6379,
        username="redis",
        password="redis"
    )


setting =Settings()