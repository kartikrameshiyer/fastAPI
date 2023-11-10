from fastapi import FastAPI , Path
from pydantic import BaseModel
from typing import Optional, List



users=[]

app= FastAPI(

    title="Mother Mary School",
    description="Following Fast API twictching streaming for studets and course implementation",
    version="0.0.1",
    contact={
        "name": "kartik",
        "email": "kartik@exmple.com",
    },
    license_info={
        "name": "MIT",
        
    },
)

class User(BaseModel):
    email : str
    is_active : bool
    bio : Optional[str] = None


@app.get("/users",response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success" 

@app.get("/user/{id}")
async def get_user(id: int= Path(...,description=" The iD of the user you want to retreive", gt=2)):
    return users[id]