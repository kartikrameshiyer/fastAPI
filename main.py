from fastapi import FastAPI 
from api import sections,courses
from api.users import router

from db.db_setup import engine
from db.models import user,course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)



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
