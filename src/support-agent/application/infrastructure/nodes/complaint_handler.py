from langchain_core.messages import AIMessage

from application.features.chat_state import ChatState
from application.infrastructure.agents.complaint_agent import ComplaintAgent

COMPLAINT_AGENT = "complaint_agent"
COMPLAINT_HUMAN = "complaint_human"
COMPLAINT_TOOLS = "tools"

def complaint_handler(state: ChatState) -> ChatState:
    print(COMPLAINT_AGENT)

    agent = ComplaintAgent()

    messages = state["messages"]

    ai_message = agent.generate_reply(messages)

    return {
        "messages": [ai_message]
    }