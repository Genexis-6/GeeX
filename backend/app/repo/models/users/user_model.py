from .. import *



class Users(Base):
    __tablename__ = "users"
    id:Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid4())
    name:Mapped[str] = mapped_column(String(100), nullable= False, index=True)
    email:Mapped[str] = mapped_column(String(100), nullable= False, unique=True, index=True)
    phone:Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(), index=True)
    verified:Mapped[Boolean] = mapped_column(Boolean, default=False, index=True)
    role:Mapped[JWTroles] = mapped_column(Enum(JWTroles, name="user_roles"), index=True, default=JWTroles.USER)
    password:Mapped[str] = mapped_column(String(255), index=True)
    
    __mapper_args__ = {
        "polymorphic_on": role,
        "polymorphic_identity": JWTroles.USER
    }