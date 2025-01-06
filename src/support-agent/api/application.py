from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .router import app_router


def create_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.include_router(app_router)
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:4200'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return fastapi_app


app = create_app()