from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class CustomerCreate(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    shipping_address: Optional[str] = None

class CustomerLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
