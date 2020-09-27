from typing import Dict

import fire
from loguru import logger

from fuse_utils.dynaconf.services.main import settings


class Main:
    def __init__(self, env: str = "development") -> None:
        settings.setenv(env)

    @staticmethod
    def project_name() -> str:
        logger.info(f"Project Name: {settings.name}")
        return settings.name

    @staticmethod
    def database(key: str = "") -> Dict[str, str]:
        if key:
            result = {key: settings.database[key]}
            logger.info(f"{key.title()}: {result}")
        else:
            result = settings.database
            logger.info(f"Database: {result}")
        return result


if __name__ == "__main__":
    fire.Fire(Main)
