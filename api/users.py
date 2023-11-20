
from typing import Optional,List

import fastapi
from sqlalchemy.orm import session
from fastapi import Path,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.utils.users import get_user,get_user_by_email,create_user,get_users
from db.db_setup import get_db, get_async_db
from pydantic_schemas.user import UserCreate, User
from pydantic_schemas.course import Course
from api.utils.courses import get_course,get_courses,get_user_courses

router = fastapi.APIRouter()

    
@router.get("/users",response_model=List[User])
async def read_users( skip: int = 0, limit: int = 100, db: session = Depends(get_db)):
    users = get_users(db,skip=skip, limit = limit)
    return users

@router.post("/users",response_model=User,status_code=201)
async def create_new_user(user : UserCreate,db: session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return create_user(db=db,user=user)

@router.get("/user/{user_id}")
async def read_user(user_id : int = Path(...,description=" The ID of the user you want to retreive"),db: AsyncSession = Depends(get_async_db)):
    db_user =await get_user(db=db,user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user


@router.get("/user/{user_id}/courses", response_model= List[Course])
async def read_user_courses(user_id: int, db : session = Depends(get_db)):
    courses = get_user_courses(user_id=user_id,db=db)
    return courses