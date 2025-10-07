from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean, Integer, UUID, ForeignKey, Enum
from ..dependecy import Base
from uuid import uuid4
from datetime import datetime
from app.utils.enums.jwt_roles import JWTroles