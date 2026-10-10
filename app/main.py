from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import close_mongo_connection, connect_to_mongo
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()


app = FastAPI(title="Simple API", lifespan=lifespan)
app.include_router(users.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
