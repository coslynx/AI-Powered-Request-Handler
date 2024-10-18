from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from api.src.models import Request
from api.src.schemas import RequestCreate, RequestSchema
from api.src.services import request_service
from api.src.database import get_db


router = APIRouter()

@router.post("/", response_model=RequestSchema, status_code=status.HTTP_201_CREATED)
async def create_request(
    request: RequestCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Handles user requests, validates input, and interacts with the request service.

    Args:
        request: The user's request data as a `RequestCreate` Pydantic model.
        db: An asynchronous session to the database.

    Returns:
        A `RequestSchema` containing the processed request and response.

    Raises:
        HTTPException: If the request data is invalid or an error occurs during processing.
    """
    try:
        db_request = Request(**request.dict())
        db.add(db_request)
        await db.commit()
        await db.refresh(db_request)
        response = await request_service.process_request(db_request.text)
        db_request.response = response
        await db.commit()
        return db_request
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing request: {e}"
        )