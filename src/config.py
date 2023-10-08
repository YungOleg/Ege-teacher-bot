from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv


load_dotenv()


@dataclass
class BotConfig:
    token: str = getenv("TOKEN")


@dataclass
class DatabaseConfig:
    url: str = getenv("DATABASE_URL")


@dataclass
class Configuration:
    # TODO: db = DatabaseConfig()
    bot = BotConfig()


config = Configuration()