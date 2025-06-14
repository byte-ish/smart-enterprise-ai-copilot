"""
Unit tests for the health check API endpoint.
"""

from fastapi.testclient import TestClient

from smart_enterprise_ai_copilot.api.main import app

client = TestClient(app)


def test_health_check():
    """
    Test that the health endpoint returns status 200 and correct JSON.
    """
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
