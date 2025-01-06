from langchain_core.messages import AIMessage

from application.features.chat_state import ChatState
from application.infrastructure.complaint_agent import ComplaintAgent

COMPLAINT_AGENT = "complaint_agent"
COMPLAINT_HUMAN = "complaint_human"

def complaint_handler(state: ChatState) -> ChatState:
    agent = ComplaintAgent()

    messages = state["messages"]

    response = agent.generate_reply(messages)

    return {
        "messages": [AIMessage(content=response)]
    }