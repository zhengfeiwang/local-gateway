import requests
from fastapi import APIRouter, Query, Request
from fastapi.responses import JSONResponse

from local_gateway.consts import AOAI_API_KEY_HEADER_NAME, AOAI_ENDPOINT_HEADER_NAME
from local_gateway.utils.redirect import create_aoai_request_headers


router = APIRouter()


# this is a test API to learn FastAPI
@router.get("/completions")
async def completions(
    request: Request,
):
    resp = {"abc": "def"}
    return JSONResponse(content=resp, status_code=200)


@router.post("/openai/deployments/{deployment_name}/chat/completions")
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
    headers = create_aoai_request_headers(api_key=request.headers.get(AOAI_API_KEY_HEADER_NAME))
    response = requests.post(url, json=request_data, headers=headers, verify=False)
    return JSONResponse(content=response.json(), status_code=200)
