# How to use local gateway on Windows

## Scenario: direct network requests

Though OpenAI has provided a Python SDK, there are still developers determined to request OpenAI API directly. This section will guide you through how to use the local gateway to trace your LLM application.

In this scenario, how you interact with the OpenAI API may look like [this snippet](./scripts/aoai-requests.py).

### 1. Install OpenSSL and generate self-signed certificate

[This page](https://slproweb.com/products/Win32OpenSSL.html) has various links, which can be very helpful; just follow this to install OpenSSL on Windows, then execute the following commands in the terminal to generate a self-signed certificate:

```bash
cd <path/to/repository>/src/local-gateway/
openssl req -x509 -nodes -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -config openssl.cnf
```

### 2. Invoke gateway service, setup interception and system proxy

```bash
# terminal #0 - invoke gateway service
cd <path/to/repository>/src/local-gateway/
python .\run.py
# another terminal #1 - setup interception
cd <path/to/repository>/src/local-gateway/
mitmproxy --mode regular -s redirect-script.py --ssl-insecure
# another terminal #2 - setup system proxy
cd <path/to/repository>/scripts/
.\interception-win.ps1 start
```

### 3. Trust `mitmproxy` in `certifi`

Add `mitmproxy` CA certificate to `certifi`, so that Python `requests` will trust `mitmproxy` and you don't need to update your code. You shall find `mitmproxy` CA certificate in `~/.mitmproxy/` directory with file name `mitmproxy-ca-cert.cer`.

```python
# locate `cacert.pem`
import certifi
print(certifi.where())
```

### 4. Run your LLM application/script...

```bash
# there is one prepared script in the repository
cd <path/to/repository>/scripts/
python .\aoai-basic.py <prompt>  # default prompt is "Wakanda Forever"
```

For your own application/script, you need to skip certificate verification, otherwise request will fail with `SSL: CERTIFICATE_VERIFY_FAILED` error.

```python
# OpenAI SDK
from openai import DefaultHttpxClient

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    http_client=DefaultHttpxClient(verify=False),  # this is the line you need to add
)

# requests.post
response = requests.post(
    ...
    verify=False,  # this is the line you need to add
)
```

### 5. Check traces

Traces by default are stored in the `<path/to/repository>/src/local-gateway/traces.json`.

You can customize the location via environment variable `GATEWAY_TRACE_DESTINATION`, for example in PowerShell:

```bash
$env:GATEWAY_TRACE_DESTINATION='C:\Users\<your-alias>\traces.json'
```

then invoke the gateway service (terminal #0).

### 6. Stop proxy

```bash
cd <path/to/repository>/scripts/
.\interception-win.ps1 stop
```
