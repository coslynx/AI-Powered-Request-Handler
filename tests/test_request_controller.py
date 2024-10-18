import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException, status
from fastapi.testclient import TestClient

from api.src.main import app
from api.src.models import Request
from api.src.schemas import RequestCreate, RequestSchema
from api.src.controllers.request_controller import router
from api.src.services.request_service import process_request
from api.src.database import get_db

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_request_success():
    """Tests successful creation and processing of a request."""
    mock_openai_response = MagicMock()
    mock_openai_response.choices = [
        {
            "message": {"content": "This is a successful OpenAI response."}
        }
    ]
    with patch("api.src.services.request_service.client.chat.completions.create", return_value=mock_openai_response), \
            patch("api.src.database.get_db", return_value=MagicMock(add=MagicMock(), commit=MagicMock(), refresh=MagicMock())):
        response = client.post(
            "/requests",
            json={"text": "Test request."},
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["response"] == "This is a successful OpenAI response."

@pytest.mark.asyncio
async def test_create_request_invalid_data():
    """Tests handling of invalid request data."""
    with patch("api.src.database.get_db", return_value=MagicMock(add=MagicMock(), commit=MagicMock(), refresh=MagicMock())):
        response = client.post(
            "/requests",
            json={"invalid_field": "Test request."},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.asyncio
async def test_create_request_openai_error():
    """Tests handling of OpenAI API errors."""
    with patch("api.src.services.request_service.client.chat.completions.create", side_effect=Exception("OpenAI API error")), \
            patch("api.src.database.get_db", return_value=MagicMock(add=MagicMock(), commit=MagicMock(), refresh=MagicMock(), rollback=MagicMock())):
        response = client.post(
            "/requests",
            json={"text": "Test request."},
        )
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert "Error processing request: OpenAI API error" in response.text

@pytest.mark.asyncio
async def test_create_request_database_error():
    """Tests handling of database errors."""
    with patch("api.src.services.request_service.process_request", return_value="Test response"), \
            patch("api.src.database.get_db", return_value=MagicMock(add=MagicMock(side_effect=Exception("Database error")), commit=MagicMock(), refresh=MagicMock(), rollback=MagicMock())):
        response = client.post(
            "/requests",
            json={"text": "Test request."},
        )
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert "Error processing request: Database error" in response.text