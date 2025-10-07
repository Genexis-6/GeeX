from .. import *
from ..users import user_model

class Sellers(user_model.Users):
    __tablename__ = "sellers"
    id:Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True, index=True)
    store_name:Mapped[str] = mapped_column(String(100), nullable=False, index=True, unique=True)
    address:Mapped[str] = mapped_column(String(255), nullable= False, index=True)
    active:Mapped[bool] = mapped_column(Boolean, default=True)
    
    __mapper_args__={
        "polymorphic_identity": JWTroles.SELLER
    }