import fastapi




router = fastapi.APIRouter()


@router.get("/sections")
async def read_sections():
    return {"courses":[]}

@router.get("/sections/{id}/content-blocks")
async def read_section_content_blocked():
    return {"courses":[]}

@router.get("content-blocks/{id}")
async def read_content_block():
    return {"courses":[]}