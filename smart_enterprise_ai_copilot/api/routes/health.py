"""
API route for health check endpoint.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/", summary="Health Check", response_description="Health status")
async def health_check():
    """
    Returns a simple JSON response indicating the service is healthy.
    """
    return JSONResponse(content={"status": "healthy"})
