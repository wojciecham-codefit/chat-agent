from langchain_core.messages import AIMessage

from application.features.chat_state import ChatState
from application.infrastructure.company_info_agent import CompanyInfoAgent

OTHER_AGENT = "other_agent"
OTHER_HUMAN = "other_human"

def other_handler(state: ChatState) -> ChatState:
    agent = CompanyInfoAgent()

    messages = state["messages"]

    response = agent.generate_reply(messages)

    return {
        "messages": [AIMessage(content=response)]
    }