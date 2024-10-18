import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException, status
from api.src.services.request_service import process_request
from api.src.models import Request
from api.src.schemas import RequestSchema

@pytest.mark.asyncio
async def test_process_request_success():
    mock_openai_response = MagicMock()
    mock_openai_response.choices = [
        {
            "message": {
                "content": "This is a successful OpenAI response.",
            }
        }
    ]
    with patch("api.src.services.request_service.client.chat.completions.create", return_value=mock_openai_response):
        text = "Test request."
        response = await process_request(text)
        assert response == "This is a successful OpenAI response."

@pytest.mark.asyncio
async def test_process_request_cache_hit():
    mock_openai_response = MagicMock()
    mock_openai_response.choices = [
        {
            "message": {
                "content": "This is a cached OpenAI response.",
            }
        }
    ]
    mock_cache = MagicMock()
    mock_cache.get.return_value = "This is a cached OpenAI response."
    with patch("api.src.services.request_service.client.chat.completions.create", return_value=mock_openai_response), \
            patch("api.src.services.request_service.cache", mock_cache):
        text = "Test request."
        response = await process_request(text)
        assert response == "This is a cached OpenAI response."
        mock_cache.get.assert_called_once_with(text)
        mock_cache.set.assert_not_called()

@pytest.mark.asyncio
async def test_process_request_cache_miss():
    mock_openai_response = MagicMock()
    mock_openai_response.choices = [
        {
            "message": {
                "content": "This is a new OpenAI response.",
            }
        }
    ]
    mock_cache = MagicMock()
    mock_cache.get.return_value = None
    with patch("api.src.services.request_service.client.chat.completions.create", return_value=mock_openai_response), \
            patch("api.src.services.request_service.cache", mock_cache):
        text = "Test request."
        response = await process_request(text)
        assert response == "This is a new OpenAI response."
        mock_cache.get.assert_called_once_with(text)
        mock_cache.set.assert_called_once_with(text, "This is a new OpenAI response.")

@pytest.mark.asyncio
async def test_process_request_openai_error():
    with patch("api.src.services.request_service.client.chat.completions.create", side_effect=Exception("OpenAI API error")):
        text = "Test request."
        with pytest.raises(HTTPException) as excinfo:
            await process_request(text)
        assert excinfo.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert "Error processing request: OpenAI API error" in str(excinfo.value.detail)