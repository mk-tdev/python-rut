from dataclasses import dataclass
import hashlib

@dataclass
class UserData:
  username: str
  nickname: str
  password_hash: str

  @staticmethod
  def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
  password = "password"
  password_hash = UserData.hash_password(password)
  print(password_hash)

  user = UserData(username="user", nickname="user", password_hash=password_hash)
  print(user)