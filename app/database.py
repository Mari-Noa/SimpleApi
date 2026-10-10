from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.config import settings

_client: AsyncIOMotorClient | None = None


async def connect_to_mongo() -> None:
    """Create the client and verify the server is reachable."""
    global _client
    _client = AsyncIOMotorClient(settings.mongo_uri, serverSelectionTimeoutMS=5000)
    await _client.admin.command("ping")


async def close_mongo_connection() -> None:
    global _client
    if _client is not None:
        _client.close()
        _client = None


def get_db() -> AsyncIOMotorDatabase:
    """FastAPI dependency that returns the app database."""
    if _client is None:
        raise RuntimeError("Mongo client is not initialised")
    return _client[settings.mongo_db_name]
