from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T  = TypeVar("T")

class DefaultApiResponse(BaseModel, Generic[T]):
    status_code:int
    message:str
    data:Optional[T] = None