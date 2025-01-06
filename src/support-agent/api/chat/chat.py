from fastapi import APIRouter

from application.dto.chat_request import ChatRequest
from application.features.flow_provider import FlowProvider

chat_router = APIRouter()


@chat_router.post("/chat")
async def send_chat_message(chat_request: ChatRequest, session_id: str | None = None):
    flow_provider = FlowProvider()

    response = flow_provider.run(session_id, chat_request.user_message)

    return response