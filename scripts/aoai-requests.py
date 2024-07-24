import os
import sys
import typing

import requests
from dotenv import load_dotenv


def main(prompt: typing.Optional[str] = None):
    if prompt is None:
        prompt = "Wakanda Forever"
    print("input prompt:", prompt)

    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    model = os.getenv("AZURE_OPENAI_MODEL")
    url = f"{endpoint}openai/deployments/{model}/chat/completions?api-version=2023-07-01-preview"
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    response = requests.post(url, headers=headers, json={"messages": messages})
    print("LLM response:")
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    prompt_from_argv = sys.argv[1] if len(sys.argv) > 1 else None
    load_dotenv()
    main(prompt=prompt_from_argv)
