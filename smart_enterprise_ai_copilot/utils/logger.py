import logging
import sys
from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Redirect standard logging to loguru
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


def setup_logging():
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    logger.configure(
        handlers=[
            {
                "sink": sys.stdout,
                "format": "<green>{time}</green> | <level>{level}</level> | <cyan>{module}</cyan> | {message}",
            }
        ]
    )
