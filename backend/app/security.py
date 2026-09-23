import os
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from dotenv import load_dotenv

load_dotenv()

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password.decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    password_bytes = password.encode("utf-8")
    password_hash_bytes = password_hash.encode("utf-8")

    return bcrypt.checkpw(password_bytes, password_hash_bytes)

def create_access_token(user_id: int) -> str:
    secret_key = os.getenv("JWT_SECRET_KEY")

    payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }

    token = jwt.encode(payload, secret_key, algorithm="HS256")

    return token

def verify_access_token(token: str) -> int:
    secret_key = os.getenv("JWT_SECRET_KEY")

    payload = jwt.decode(
        token,
        secret_key,
        algorithms=["HS256"],
    )

    user_id = int(payload["sub"])

    return user_id