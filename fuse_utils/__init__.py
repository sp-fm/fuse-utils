"""Top-level package for Fusemachines Utilities."""

__author__ = """Shashanka Prajapati"""
__email__ = "shashanka@fusemachines.com"
__version__ = "0.1.0"

import logging

from loguru import logger

logger.add("logs/critical.log", level="CRITICAL", rotation="10MB")
logger.add("logs/error.log", level="ERROR", rotation="10MB")
logger.add("logs/warning.log", level="WARNING", rotation="10MB")
logger.add("logs/info.log", level="INFO", rotation="10MB")
logger.add("logs/debug.log", level="DEBUG", rotation="10MB")


# Required for log testing
# https://github.com/Delgan/loguru/issues/59
class PropagateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


logger.add(PropagateHandler(), format="{message}")