from pydantic import BaseModel, validator
import re

class RequestCreate(BaseModel):
    text: str

    @validator("text")
    def validate_text(cls, value):
        if not value:
            raise ValueError("Request text is required.")
        # Sanitize input to prevent XSS
        value = re.sub(r"<[^>]+>", "", value)
        # Additional validation rules can be added here
        return value