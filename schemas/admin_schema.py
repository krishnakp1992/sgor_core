# build a schema using pydantic
from pydantic import BaseModel, Field, EmailStr, root_validator
from datetime import datetime
from typing import Optional


class CreateSportsGear(BaseModel):
    name: str = Field(min_length=5)
    sport: Optional[str]
    available_count: int
    class Config:
        orm_mode = True


class UpdateSportsGear(BaseModel):
    name: Optional[str] = None
    sport: Optional[str] = None
    available_count: Optional[int] = None
    class Config:
        orm_mode = True

class ListSportsGear(BaseModel):
    name: Optional[str] = None
    sport: Optional[str] = None
    available_count: Optional[int] = None
    time_created: datetime
    id: Optional[int] = None
    class Config:
        orm_mode = True

class ListUser(BaseModel):
    name:str 
    email:str
    phone_number:str
    address:str
    # is_admin:bool

    class Config:
        orm_mode = True

class CreateUser(BaseModel):
    name:str = Field(min_length=5)
    email:EmailStr
    phone_number: Optional[str]
    address: Optional[str]
    password :str = Field(min_length=5)
    confirm_password :str = Field(min_length=5)
    # is_admin:bool

    @root_validator()
    def verify_password_match(cls,values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise ValueError("The two passwords did not match.")
        return values
        