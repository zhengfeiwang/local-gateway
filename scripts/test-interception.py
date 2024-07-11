import requests

response = requests.get("http://www.baidu.com")
assert "baidu" in response.text, response.text
response = requests.get("http://www.google.com")
assert "google" not in response.text, response.text
print("test passed!")
