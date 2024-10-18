from typing import Optional
from fastapi import HTTPException, status
from openai import OpenAI
from api.src.models import Request
from api.src.config import settings
from api.src.utils.cache import cache
from fastapi.responses import JSONResponse

client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def process_request(text: str) -> str:
    """
    Processes user requests, translates them into OpenAI API calls, and returns formatted responses.

    Args:
        text: The user's request text.

    Returns:
        A formatted OpenAI response.

    Raises:
        HTTPException: If an error occurs during request processing or OpenAI API call.
    """
    try:
        # Check if the request is cached
        cached_response = await cache.get(text)
        if cached_response:
            return cached_response

        # Construct the OpenAI API call
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text}
            ],
            temperature=0.7,  # Adjust as needed
            max_tokens=1000,  # Adjust as needed
        )

        # Process the OpenAI response
        formatted_response = response.choices[0].message.content

        # Cache the response for future requests
        await cache.set(text, formatted_response)

        return formatted_response

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing request: {e}",
        )