import io

from langchain_core.runnables.graph import MermaidDrawMethod
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from PIL import Image

from application.features.chat_state import ChatState
from application.infrastructure.nodes.agent_routing import AGENT_ROUTING_NODE, agent_routing_node
from application.infrastructure.nodes.category_evaluator import CATEGORY_EVALUATOR, evaluate_category_node
from application.infrastructure.nodes.complaint_handler import COMPLAINT_AGENT, COMPLAINT_HUMAN, complaint_handler
from application.infrastructure.nodes.end_node import END_NODE, end_node
from application.infrastructure.nodes.human_inerrupt import human_interrupt
from application.infrastructure.nodes.other_handler import OTHER_AGENT, OTHER_HUMAN, other_handler
from application.infrastructure.nodes.should_continue import SHOULD_CONTINUE_NODE, should_continue

memory = MemorySaver()

workflow = StateGraph(ChatState)
workflow.add_node(CATEGORY_EVALUATOR, evaluate_category_node)
workflow.add_node(OTHER_AGENT, other_handler)
workflow.add_node(COMPLAINT_AGENT, complaint_handler)
workflow.add_node(COMPLAINT_HUMAN, human_interrupt)
workflow.add_node(OTHER_HUMAN, human_interrupt)
workflow.add_node(END_NODE, end_node)
workflow.set_entry_point(CATEGORY_EVALUATOR)

workflow.add_conditional_edges(CATEGORY_EVALUATOR, agent_routing_node)
workflow.add_edge(COMPLAINT_HUMAN, COMPLAINT_AGENT)
workflow.add_conditional_edges(OTHER_AGENT, should_continue)
workflow.add_conditional_edges(COMPLAINT_AGENT, should_continue)
workflow.add_edge(OTHER_HUMAN, OTHER_AGENT)

flow = workflow.compile(checkpointer=memory)

image_bytes = flow.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.API)
Image.open(io.BytesIO(image_bytes)).save("graph.png")