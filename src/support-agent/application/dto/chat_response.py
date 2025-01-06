from pydantic import BaseModel


class ChatResponse(BaseModel):
    session_id: str
    llm_response: str
    finish: bool