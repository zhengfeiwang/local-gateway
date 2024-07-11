from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/completions")
async def completions(
    request: Request,
):
    resp = {"abc": "def"}
    return JSONResponse(content=resp, status_code=200)
