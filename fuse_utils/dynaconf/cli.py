import fire
from loguru import logger

from fuse_utils.dynaconf.services.main import settings


class Main:
    def __init__(self, env: str = "default") -> None:
        settings.setenv(env)

    @staticmethod
    def package_name() -> None:
        logger.info(f"Package Name: {settings.name}")

    @staticmethod
    def database(key: str = "") -> None:
        if key:
            logger.info(f"{key.title()}: {settings.database[key]}")
        else:
            logger.info(f"Database: {settings.database}")


if __name__ == "__main__":
    fire.Fire(Main)
