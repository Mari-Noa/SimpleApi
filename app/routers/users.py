from fastapi import APIRouter, Depends, HTTPException, Response, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.database import get_db
from app.models import UserIn, UserOut

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    doc = await db.users.find_one({"_id": user_id})
    if doc is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    doc["id"] = doc.pop("_id")
    return doc


@router.put("/{user_id}", response_model=UserOut)
async def put_user(
    user_id: str,
    user: UserIn,
    response: Response,
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    """Create the user if the id is new, otherwise replace it."""
    result = await db.users.replace_one(
        {"_id": user_id}, user.model_dump(), upsert=True
    )
    response.status_code = (
        status.HTTP_201_CREATED if result.upserted_id is not None else status.HTTP_200_OK
    )
    return UserOut(id=user_id, **user.model_dump())
