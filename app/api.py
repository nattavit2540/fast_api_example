# app/api.py
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from .schemas import UserCreate, User
from .services import create_user_service
from sqlalchemy.orm import Session
from database import SessionLocal  # You would define SessionLocal using SQLAlchemy's sessionmaker

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=User)
async def create_user(user: UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    created_user = await create_user_service(user=user)
    if not created_user:
        raise HTTPException(status_code=400, detail="Error creating user.")
    # Assume `send_welcome_email` is a function you'd call as a background task
    background_tasks.add_task(send_welcome_email, user.email)
    return created_user
