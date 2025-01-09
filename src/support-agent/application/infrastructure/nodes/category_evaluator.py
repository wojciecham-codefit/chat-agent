from application.features.chat_state import ChatState
from application.infrastructure.agents.association_agent import AssociationAgent
from domain.request_category import RequestCategory

CATEGORY_EVALUATOR = "category_evaluator"

def evaluate_category_node(state: ChatState) -> ChatState:
    agent = AssociationAgent()

    response = agent.check_category(state["messages"])

    category = RequestCategory.from_string(response)

    return {
        "category": category
    }