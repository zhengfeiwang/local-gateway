from fastapi import FastAPI

from local_gateway.api.v1.routes import router

app = FastAPI(
    title="Local Gateway",
)

app.include_router(router)
