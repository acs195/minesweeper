"""This is the logger module"""

import logging
import sys

from core.config import get_settings

settings = get_settings()


def get_logger() -> logging.Logger:
    """Get custom logger"""
    logger = logging.getLogger(settings.PROJECT_NAME)
    logger.setLevel(settings.LOG_LEVEL)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


logger = get_logger()
