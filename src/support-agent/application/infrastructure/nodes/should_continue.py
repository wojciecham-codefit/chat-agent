from numpy.random import RandomState

from application.features.chat_state import ChatState
from application.infrastructure.nodes.agent_routing import AGENT_ROUTING_NODE
from application.infrastructure.nodes.complaint_handler import COMPLAINT_AGENT, COMPLAINT_HUMAN
from application.infrastructure.nodes.end_node import END_NODE
from application.infrastructure.nodes.other_handler import OTHER_HUMAN
from domain.request_category import RequestCategory

SHOULD_CONTINUE_NODE = "should_continue"

FINISH_MESSAGE = "KONIEC"

def should_continue(state: ChatState) -> str:
    if FINISH_MESSAGE in state["messages"][-1].content:
        return END_NODE
    else:
        if state["category"] is RequestCategory.COMPLAINT:
            return COMPLAINT_HUMAN
        else:
            return OTHER_HUMAN

