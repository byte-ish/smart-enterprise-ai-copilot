# Stage 1: Build dependencies and install packages
FROM python:3.12-slim AS builder

# Install system dependencies for Poetry and build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential libffi-dev gcc git && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry (latest stable, no version pin)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy pyproject.toml and poetry.lock first for caching
COPY pyproject.toml poetry.lock* /app/

# Install dependencies without creating virtualenv (install globally in container)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copy project code
COPY . /app

# Stage 2: Create final lightweight image
FROM python:3.12-slim

WORKDIR /app

# Copy installed dependencies and source code from builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

# Set environment variables for optimal Python behavior in containers
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "smart_enterprise_ai_copilot.api.main:app", "--host", "0.0.0.0", "--port", "8000"]