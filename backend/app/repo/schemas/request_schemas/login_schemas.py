from pydantic import BaseModel


class LoginSchemas(BaseModel):
    username: str
    password: str