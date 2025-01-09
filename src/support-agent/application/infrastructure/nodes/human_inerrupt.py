from langchain_core.messages import HumanMessage
from langgraph.types import interrupt

from application.features.chat_state import ChatState


def human_interrupt(state: ChatState) -> ChatState:
    print("HUMAN_NODE")
    human_message = interrupt(state["messages"][-1])

    return {
        "messages": [HumanMessage(content=human_message)]
    }