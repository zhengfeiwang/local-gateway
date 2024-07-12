## How to use local gateway (Windows)

### 1. Install OpenSSL and generate self-signed certificate

[This page](https://slproweb.com/products/Win32OpenSSL.html) has various links, which can be very helpful.

```bash
cd src/local-gateway/
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem
```

### 2. Invoke intercepting proxy and set proxy for the system

```bash
cd src/local-gateway/
mitmproxy --mode regular -s redirect-script.py --ssl-insecure
cd ../../scripts/
.\interception-win.ps1 start
```
