from typing import TypedDict, Annotated, List

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph.message import add_messages

from domain.request_category import RequestCategory


class ChatState(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], add_messages]
    category: RequestCategory | None
    finish: bool