from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/completions")
async def completions(
    request: Request,
):
    resp = {"abc": "def"}
    return JSONResponse(content=resp, status_code=200)


@router.post(
    "/openai/deployments/{deployment_name}/chat/completions"
)
async def chat_completions(
    request_data: dict,
    request: Request,
    deployment_name=None,
    api_path=None,
):
    resp = {
        "api": "mocked",
        "endpoint": request.headers.get("endpoint"),
        "deployment_name": deployment_name,
    }
    return JSONResponse(content=resp, status_code=200)
