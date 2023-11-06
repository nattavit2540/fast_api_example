# app/services.py
from . import crud, schemas

# This is a very simplistic service layer.
# In a real-world application, you'd have more complex logic here.
async def create_user_service(user: schemas.UserCreate):
    # Assume we have a `db_session` dependency that provides a SQLAlchemy session.
    user = await crud.create_user(db_session, user=user)
    return user
