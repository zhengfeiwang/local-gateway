import requests
from fastapi import APIRouter, Query, Request
from fastapi.responses import JSONResponse

from local_gateway.consts import AOAI_ENDPOINT_HEADER_NAME


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
    api_version=Query(None, alias="api-version"),
):
    endpoint = request.headers.get(AOAI_ENDPOINT_HEADER_NAME)
    if endpoint is None:
        raise Exception("endpoint not available")
    url = (
        f"https://{endpoint}.openai.azure.com/openai/deployments/{deployment_name}/"
        f"chat/completions?api-version={api_version}"
    )
    headers = {
        "content-type": "application/json",
        "api-key": request.headers.get("api-key"),
        "no-interception": "true",
    }
    response = requests.post(url, json=request_data, headers=headers, verify=False)
    return JSONResponse(content=response.json(), status_code=200)
