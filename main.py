from fastapi import FastAPI , Path
from pydantic import BaseModel
from typing import Optional, List
from api import sections,courses
from api.users import router



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

app.include_router(router)
app.include_router(sections.router)
app.include_router(courses.router)


