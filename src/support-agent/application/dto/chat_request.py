﻿from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_message: str