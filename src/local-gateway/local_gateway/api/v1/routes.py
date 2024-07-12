from fastapi import APIRouter, Request
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
@router.post(
    "//openai/deployments/{deployment_name}/chat/completions"
)
async def chat_completions(
    request_data: dict,
    request: Request,
    deployment_name=None,
    api_path=None,
):
    # resp = {
    #     "api": "mocked",
    #     "endpoint": request.headers.get(AOAI_ENDPOINT_HEADER_NAME),
    #     "deployment_name": deployment_name,
    # }
    const_resp = {
        "choices": [
            {
                "content_filter_results": {
                    "hate": {
                        "filtered": False,
                        "severity": "safe"
                    },
                    "self_harm": {
                        "filtered": False,
                        "severity": "safe"
                    },
                    "sexual": {
                        "filtered": False,
                        "severity": "safe"
                    },
                    "violence": {
                        "filtered": False,
                        "severity": "safe"
                    }
                },
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": "Hi there! How can I assist you today?",
                    "role": "assistant"
                }
            }
        ],
        "created": 1720771366,
        "id": "chatcmpl-9k5WoIgk769Jh7w47SxkyoY7q91Zv",
        "model": "gpt-4",
        "object": "chat.completion",
        "prompt_filter_results": [
            {
                "prompt_index": 0,
                "content_filter_results": {
                    "hate": {
                        "filtered": False,
                        "severity": "safe"
                    },
                    "self_harm": {
                        "filtered": False,
                        "severity": "safe"
                    },
                    "sexual": {
                        "filtered": False,
                        "severity": "safe"
                    },
                    "violence": {
                        "filtered": False,
                        "severity": "safe"
                    }
                }
            }
        ],
        "system_fingerprint": None,
        "usage": {
            "completion_tokens": 10,
            "prompt_tokens": 19,
            "total_tokens": 29
        }
    }
    return JSONResponse(content=const_resp, status_code=200)
