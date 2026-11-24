from argon2 import PasswordHasher, Type
from argon2.exceptions import InvalidHashError, VerifyMismatchError


_hasher = PasswordHasher(type=Type.ID)


def hash_password(password: str) -> str:
    return _hasher.hash(password)


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        return _hasher.verify(stored_hash, password)
    except (VerifyMismatchError, InvalidHashError):
        return False
