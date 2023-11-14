
from typing import Optional,List

import fastapi
from sqlalchemy.orm import session
from fastapi import Path,Depends,HTTPException

from api.utils.users import get_user,get_user_by_email,create_user,get_users
from db.db_setup import get_db
from pydantic_schemas.user import UserCreate, User

router = fastapi.APIRouter()

    
@router.get("/users",response_model=List[User])
async def read_users( skip: int = 0, limit: int = 100, db: session = Depends(get_db)):
    users = get_users(db,skip=skip, limit = limit)
    return users

@router.post("/users")
async def create_new_user(user : UserCreate,db: session = Depends(get_db)):
    return create_user(db=db,user=user)

@router.get("/user/{user_id}")
async def read_user(user_id : int = Path(...,description=" The iD of the user you want to retreive"),db: session = Depends(get_db)):
    return get_user(db=db,user_id=user_id)