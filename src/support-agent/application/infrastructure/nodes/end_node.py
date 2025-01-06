from langchain_core.messages import AIMessage

from application.features.chat_state import ChatState

FINAL_MESSAGE = """
    Dziękuje za współpracę, jeżeli będziesz czegoś potrzebował naciśnij 'Nowa konwersacja' lub odśwież stronę.
    W następnej wiadomości możesz napisać ocenę mojej pracy (w skali 1 do 5) oraz/lub napisać komentarz na temat
    mojej pracy.
"""

END_NODE = "end_node"

def end_node(state: ChatState) -> ChatState:
    return {
        "messages": [AIMessage(content=FINAL_MESSAGE)],
        "finish": True,
    }