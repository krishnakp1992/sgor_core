import pytz
from sqlalchemy import text
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()


class SportsGear(Base):
    __tablename__ = 'sports_gear'
    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sport = Column(String)
    available_count  = Column(Integer, nullable=False)
    rent_per_day = Column(Float, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    created_by = relationship('User')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    phone_number = Column(String)
    address = Column(String)
    is_admin = Column(Boolean, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class UserRental(Base):
    __tablename__ = 'user_rental'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    sports_gear_id = Column(Integer, ForeignKey('sports_gear.id'))
    rented_sports_gear_count  = Column(Integer, nullable=False)
    user_requested_duration_in_days  = Column(Integer, nullable=False)
    rental_started = Column(DateTime(timezone=True), server_default=func.now())
    rental_end_date = Column(DateTime(timezone=True), onupdate=func.now())
    total_rent = Column(Float, nullable=False)
    created_by = relationship('User')
    sports_gear = relationship('SportsGear')


