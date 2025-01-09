import io

from langchain_core.runnables.graph import MermaidDrawMethod
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, END
from PIL import Image
from langgraph.prebuilt import ToolNode, tools_condition

from application.features.chat_state import ChatState
from application.infrastructure.nodes.agent_routing import AGENT_ROUTING_NODE, agent_routing_node
from application.infrastructure.nodes.category_evaluator import CATEGORY_EVALUATOR, evaluate_category_node
from application.infrastructure.nodes.complaint_handler import COMPLAINT_AGENT, COMPLAINT_HUMAN, complaint_handler, \
    COMPLAINT_TOOLS
from application.infrastructure.nodes.dummy_node import DUMMY_NODE, dummy_handler
from application.infrastructure.nodes.end_node import END_NODE, end_node
from application.infrastructure.nodes.human_inerrupt import human_interrupt
from application.infrastructure.nodes.other_handler import OTHER_AGENT, OTHER_HUMAN, other_handler
from application.infrastructure.nodes.should_continue import SHOULD_CONTINUE_NODE, should_continue
from application.infrastructure.tools.add_complaint import add_complaint
from application.infrastructure.tools.check_complaint import check_complaint


memory = MemorySaver()

workflow = StateGraph(ChatState)

complaint_tool_node = ToolNode([add_complaint, check_complaint])

workflow.add_node(CATEGORY_EVALUATOR, evaluate_category_node)
workflow.add_node(OTHER_AGENT, other_handler)
workflow.add_node(COMPLAINT_AGENT, complaint_handler)
workflow.add_node(COMPLAINT_HUMAN, human_interrupt)
workflow.add_node(OTHER_HUMAN, human_interrupt)
workflow.add_node(END_NODE, end_node)
workflow.set_entry_point(CATEGORY_EVALUATOR)
workflow.add_node(COMPLAINT_TOOLS, complaint_tool_node)
workflow.add_node(DUMMY_NODE, dummy_handler)

workflow.add_conditional_edges(CATEGORY_EVALUATOR, agent_routing_node)
workflow.add_edge(COMPLAINT_HUMAN, COMPLAINT_AGENT)
workflow.add_conditional_edges(OTHER_AGENT, should_continue)
workflow.add_conditional_edges(COMPLAINT_AGENT, tools_condition, path_map={ "tools": COMPLAINT_TOOLS, "__end__": DUMMY_NODE })
workflow.add_edge(OTHER_HUMAN, OTHER_AGENT)
workflow.add_edge(COMPLAINT_TOOLS, COMPLAINT_AGENT)
workflow.add_conditional_edges(DUMMY_NODE, should_continue)

flow = workflow.compile(checkpointer=memory)

image_bytes = flow.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.API)
Image.open(io.BytesIO(image_bytes)).save("graph.png")