from fastapi import APIRouter

home_router = APIRouter()


@home_router.get("/")
def health() -> str:
    return "It Works!"

@home_router.get("/version")
def version() -> str:
    return "0.0.0"
