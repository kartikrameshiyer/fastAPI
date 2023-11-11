import fastapi
from typing import Optional,List
from pydantic import BaseModel
from fastapi import Path


router = fastapi.APIRouter()

users=[]

class User(BaseModel):
    email : str
    is_active : bool
    bio : Optional[str] = None
@router.get("/users",response_model=List[User])
async def get_users():
    return users
@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success" 
@router.get("/user/{id}")
async def get_user(id: int= Path(...,description=" The iD of the user you want to retreive", gt=2)):
    return users[{"id": "1" }]