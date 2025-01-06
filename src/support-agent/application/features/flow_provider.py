import uuid

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.types import Command

from application.dto.chat_response import ChatResponse
from application.features.chat_state import ChatState
from application.features.workflow_generator import flow


class FlowProvider:
    def run(self, session_id: str | None, user_message: str):
        current_state: ChatState = self._create_empty_state(user_message)
        current_session_id = session_id

        if session_id is None or session_id == "":
            current_session_id = str(uuid.uuid4())
            thread_config = {"configurable": {"thread_id": current_session_id}}
            current_state = flow.invoke(current_state, thread_config)
        else:
            thread_config = {"configurable": {"thread_id": current_session_id}}
            current_state = flow.invoke(Command(resume=user_message), thread_config)

        last_response = current_state["messages"][-1]

        last_message = ""

        if last_response is not None and isinstance(last_response, AIMessage):
            last_message = last_response.content

        return ChatResponse(session_id=current_session_id, llm_response=last_message, finish=current_state["finish"])

    def _create_empty_state(self, user_message: str) -> ChatState:
        return ChatState(
            messages=[HumanMessage(content=user_message)],
            category=None,
            finish=False,
        )



