from application.features.chat_state import ChatState
from application.infrastructure.nodes.complaint_handler import COMPLAINT_AGENT
from application.infrastructure.nodes.other_handler import OTHER_AGENT
from domain.request_category import RequestCategory

AGENT_ROUTING_NODE = "agent_routing_node"

def agent_routing_node(state: ChatState) -> str:
    if state["category"] is RequestCategory.COMPLAINT:
        return COMPLAINT_AGENT
    else:
        return OTHER_AGENT