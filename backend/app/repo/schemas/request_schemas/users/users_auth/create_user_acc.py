from pydantic import BaseModel, Field, EmailStr

class CreateUserAccountSchemas(BaseModel):
    name: str = Field(max_length=99, min_length=4, description="enter your full name")
    email: EmailStr
    phone: str = Field(max_length=20, min_length=10, description="enter your phone number")
    password: str = Field(max_length= 16, min_length=7, description="enter you password")
    
    
    
