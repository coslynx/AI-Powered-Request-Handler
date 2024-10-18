from fastapi import HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from typing import Optional

from api.src.utils.jwt_utils import decode_jwt_token

class JWTAuthentication(HTTPBearer):
    """
    Implements JWT authentication middleware for protecting API routes.

    This middleware intercepts incoming API requests and verifies the presence
    and validity of a JWT token. It then extracts the user ID from the decoded
    token and attaches it to the request object.

    Args:
        request:  The FastAPI request object.

    Returns:
        The decoded JWT token payload (containing user ID) if authentication
        is successful.

    Raises:
        HTTPException: If the token is missing or invalid.
    """
    async def __call__(self, request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            try:
                payload = decode_jwt_token(credentials.credentials)
                request.state.user_id = payload['sub']
                return payload
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token",
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required"
            )