from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from application.infrastructure.llm_provider import LlmProvider

message_template = """
Jesteś pomocnym asystentem, którego celem jest skategaryzować zapytanie klienta,
pierwsza kategoria: complaint, gdy dotyczy ono reklamacji. Druga kategoria purchase,
gdy dotyczy chęci zapytania o produkt - informacyjnie lub aby zakupić. Trzecia kategoria:
return, gdy dotyczy ono zwrotu produktu. Jeżeli zaoytanie klienta nie pasuje do żadnej, to skategoryzuj jako other.
W odpowiedzi w pierwszej linijce koniecznie napisz nazwę kategorii, czyli complaint, purchase, return lub other.
Jeżeli nie masz wystarczająco informacji, by skategoryzwać, to napisz krótką informację dla użytkownika o sprecyzowanie
co chciały zrobić. Nie odpowiadaj na żadne pytania użytkownika.
"""

class AssociationAgent:
    _llm: BaseChatModel

    def __init__(self):
        self._llm = LlmProvider().get_llm()

    def check_category(self, messages: list[AIMessage | HumanMessage]) -> str:
        chat_messages = [SystemMessage(message_template)] + messages

        response = self._llm.invoke(chat_messages)

        return response.content
