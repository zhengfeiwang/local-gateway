import uvicorn

from local_gateway.consts import GATEWAY_PORT


def main():
    uvicorn.run(
        "local_gateway.app:app",
        host="0.0.0.0",
        port=GATEWAY_PORT,
        ssl_certfile="cert.pem",
        ssl_keyfile="key.pem",
        reload=True,
    )


if __name__ == "__main__":
    main()
