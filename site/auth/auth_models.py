from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    animals: Optional[list] = None
    hashed_password: Optional[str] = None


class UserInDB(User):
    hashed_password: str
