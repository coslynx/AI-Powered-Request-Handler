from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .models import User
from .routers import users, requests
from .auth import JWTAuthentication
from .config import settings

app = FastAPI()

# Database setup
async def get_db():
    async with AsyncSession(engine) as session:
        yield session

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(
    requests.router,
    prefix="/requests",
    tags=["requests"],
    dependencies=[Depends(JWTAuthentication)],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()