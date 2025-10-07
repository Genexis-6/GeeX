from .dependecy import AsyncSession, db_session_manager
from fastapi import Depends
from typing_extensions import Annotated


# linking models to app
from .models.register_model import *



async def get_db():
    async with db_session_manager.session() as session:
        yield session
        
        


db_injection = Annotated[AsyncSession, Depends(get_db)]