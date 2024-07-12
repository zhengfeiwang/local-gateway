import os

from dotenv import load_dotenv
from openai import AzureOpenAI, DefaultHttpxClient

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    http_client=DefaultHttpxClient(verify=False),
)
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Wakanda Forever"},
]
chat_completion = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
)
print(chat_completion.choices[0].message.content)
