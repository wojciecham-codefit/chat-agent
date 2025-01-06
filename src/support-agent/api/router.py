from fastapi import APIRouter

from api.chat.chat import chat_router
from api.home.home import home_router

api_prefix = '/api'

app_router = APIRouter()
app_router.include_router(chat_router, prefix=api_prefix)
app_router.include_router(home_router)