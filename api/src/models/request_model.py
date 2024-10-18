from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from api.src.config import settings  # Use settings.py for environment variables
from api.src.utils.cache import cache  # Import cache for caching responses (if using)

Base = declarative_base()


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)  # Database ID
    user_id = Column(Integer, nullable=False)  # User ID (link to users table)
    text = Column(String, nullable=False)  # User's request text
    response = Column(String, nullable=True)  # OpenAI response (store it for future reference)
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for creation time
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp for updates