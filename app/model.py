# app/models.py
from sqlalchemy import Column, Integer, String
from database import Base  # You would define Base using SQLAlchemy's declarative_base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
