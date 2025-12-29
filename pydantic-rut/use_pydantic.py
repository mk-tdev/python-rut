from pydantic import BaseModel, field_validator, ConfigDict, validator
from __future__ import annotations
import hashlib


class UserData(BaseModel):
  username: str
  nickname: str
  password_hash: str

  @field_validator("password_hash", mode="before")
  @classmethod
  def hash_password(cls, v: str) -> str:
    if not v or not isinstance(v, str):
      raise ValueError("Password hash must be a string")

    return hashlib.sha256(v.encode()).hexdigest()

  @validator("username")
  @classmethod
  def validate_username(cls, v: str) -> str:
    if not v or not isinstance(v, str):
      raise ValueError("Username must be a string")

    return v

  model_config = ConfigDict(
    extra="forbid"
  )

if __name__ == "__main__":
  user = UserData(username="user", nickname="user", password_hash="password")
  print(user)
  user.dict()