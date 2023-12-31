# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

async def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

async def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
