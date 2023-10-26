# build a schema using pydantic
import pytz
from pydantic import BaseModel, Field, EmailStr, root_validator, validator
from datetime import datetime
from typing import Optional


class CreateSportsGear(BaseModel):
    name: str = Field(min_length=5)
    sport: Optional[str]
    available_count: int
    rent_per_day: float
    class Config:
        orm_mode = True


class UpdateSportsGear(BaseModel):
    name: Optional[str] = None
    sport: Optional[str] = None
    available_count: Optional[int] = None
    rent_per_day: Optional[float] = None
    class Config:
        orm_mode = True

class ListSportsGear(BaseModel):
    name: Optional[str] = None
    sport: Optional[str] = None
    available_count: Optional[int] = None
    rent_per_day: Optional[float] = None
    time_created: str
    id: Optional[int] = None
    class Config:
        orm_mode = True

    @validator("time_created", pre=True, always=True)
    def convert_to_indian_time(cls, value):
        # Define the UTC and IST time zones
        utc_timezone = pytz.timezone("UTC")
        ist_timezone = pytz.timezone("Asia/Kolkata")  # Use the appropriate time zone

        if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
            # Assuming the input is in UTC, if it has no timezone information
            value = utc_timezone.localize(value)

        # Convert the time_created to IST
        value = value.astimezone(ist_timezone)
        formatted_time = value.strftime("%d-%m-%y %H:%M:%S")

        return formatted_time

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

class UpdateUser(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None


class RentSportsGear(BaseModel):
    item_count: int
    rental_duration: int
