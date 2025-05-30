"""
Main FastAPI application initialization and middleware setup.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from smart_enterprise_ai_copilot.api.middleware.exception_handler import (
    ExceptionHandlingMiddleware,
)
from smart_enterprise_ai_copilot.api.routes.health import router as health_router
from smart_enterprise_ai_copilot.utils.logger import setup_logging

# Initialize logging
setup_logging()

app = FastAPI(
    title="Smart Enterprise AI Copilot",
    description="A modular, production-grade AI agent platform.",
    version="0.1.0",
)

# Add exception handling middleware
app.add_middleware(ExceptionHandlingMiddleware)

# Add CORS middleware with all origins allowed for development.
# NOTE: Restrict allowed origins for production deployments.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # NOTE: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(health_router, prefix="/health", tags=["Health"])
