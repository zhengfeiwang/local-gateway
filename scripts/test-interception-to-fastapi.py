import requests

response = requests.get("http://www.openai.com/completions")
print(response.text)
resp_dict = response.json()
assert resp_dict == {"abc": "def"}, resp_dict
print("test passed!")
