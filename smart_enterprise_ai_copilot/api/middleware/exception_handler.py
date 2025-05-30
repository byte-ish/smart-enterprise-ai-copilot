"""
Middleware for global exception handling in the FastAPI application.
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


class ExceptionHandlingMiddleware(BaseHTTPMiddleware): # pylint: disable=too-few-public-methods
    """
    Middleware to catch unhandled exceptions, log them, and return
    a standardized 500 Internal Server Error response.
    """

    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:  # pylint: disable=broad-exception-caught
            logger.error(f"Unhandled Exception: {exc}", exc_info=True)
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"},
            )
