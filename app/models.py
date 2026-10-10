from pydantic import BaseModel, EmailStr, Field


class UserIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int | None = Field(default=None, ge=0, le=150)


class UserOut(UserIn):
    id: str
