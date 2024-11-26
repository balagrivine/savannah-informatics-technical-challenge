from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class CustomerCreate(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    phone_number: str = Field(..., max_length=12, min_length=10)

class CustomerLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
