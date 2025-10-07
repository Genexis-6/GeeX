from enum import Enum


class JWTroles(Enum):
    SELLER:str = "sellers"
    ADMIN: str = "admin"
    USER: str = "users"
    