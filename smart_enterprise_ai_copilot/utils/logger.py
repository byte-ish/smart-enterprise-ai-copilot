"""
Logging setup module using Loguru with redirection of standard logging.
"""

import logging
import sys
from loguru import logger


class InterceptHandler(logging.Handler):
    """
    Handler to redirect standard logging to Loguru.
    """

    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


def setup_logging():
    """
    Configure the root logger to intercept logs and send them to Loguru,
    with a colored and structured output format.
    """
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    logger.configure(
        handlers=[
            {
                "sink": sys.stdout,
                "format": (
                    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                    "<level>{level: <8}</level> | "
                    "<cyan>{module}</cyan> | "
                    "{message}"
                ),
            }
        ]
    )
