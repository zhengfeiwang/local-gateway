import os
import sys
import typing

from dotenv import load_dotenv
from openai import AzureOpenAI, DefaultHttpxClient


def main(prompt: typing.Optional[str] = None):
    if prompt is None:
        prompt = "Wakanda Forever"
    print("input prompt:", prompt)
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2023-12-01-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        http_client=DefaultHttpxClient(verify=False),
    )
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
    )
    print("LLM response:", chat_completion.choices[0].message.content)


if __name__ == "__main__":
    prompt_from_argv = sys.argv[1] if len(sys.argv) > 1 else None
    load_dotenv()
    main(prompt=prompt_from_argv)
