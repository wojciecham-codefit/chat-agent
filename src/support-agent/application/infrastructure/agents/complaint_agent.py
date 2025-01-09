from langchain_core.language_models import BaseChatModel, LanguageModelInput
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
from langchain_core.runnables import Runnable

from application.infrastructure.llm_provider import LlmProvider
from application.infrastructure.tools.add_complaint import add_complaint
from application.infrastructure.tools.check_complaint import check_complaint

message_template = """
Jesteś pomocnym asystentem, którego celem jest zebranie odpowiednich informacji
do przyjęcia zgłoszenia reklamacji. Sklep dla, którego przyjmujesz reklamację nazywa się
Qpik i zajmuje się sprzedażą internetową. 
Twoim zadaniem jest przyjęcie nowej reklamacji lub odpowiedzenie jaki status jest obecnej
istniejącej reklamacji.
Do przyjęcia reklamacji potrzebujesz 10-cyfrowy numer zamówienia, powód reklamacji oraz adres e-mail osoby, ale nie pytaj o informacje, które już podał.
Jeżeli posiadasz wszystkie dane, to użyj narzędzia add_complaint - powinieneś je mieć na liście swoich narzędzi
, by dodać reklamacje do systemu, a następnie odpisz, że dziękujesz za podanie informacji i reklamacja została przyjęta, dodaj
jeszcze, czy możesz w czymś pomóc jeszcze, jeżeli użytkownik odpisze w jakikolwiek sposób, że nie potrzebuje już w niczym
więcej pomocy, to napisz po prostu samo *KONIEC*
Jeżeli użytkownik chce byś sprawdził status reklamacji, potrzebujesz 10 cyfrowy numer zamówienia
gdy poda go poprawnie możesz użyć narzędzia check_complaint - powinieneś je mieć na liście swoich narzędzi, by sprawdzić status reklamacji
zostanie on zwrócony opisowo w postaci tekstu. Przeanalizuj rezultat i odpisz użytkownikowi
jak tam jego reklamacja. Oczywiście zapytaj potem, czy potrzebuje czegoś jeszcze, jeżeli nie, to napisz
samo *KONIEC*.
Jeżeli numer zamówienia jest niepoprawny, bo nie jest 10-cyfrowy lub adres email jest niepoprawnie sformatowany, to wyjaśnij
że jest niepoprawna wartość i poproś o powtórzenie.
Nie odpowiadaj na inne pytania dotyczące świata, tylko skup się na tym swoim zadaniu.
"""

class ComplaintAgent:
    _llm: Runnable[LanguageModelInput, BaseMessage]

    def __init__(self):
        tools = [add_complaint, check_complaint]
        self._llm = LlmProvider().get_llm().bind_tools(tools=tools)


    def generate_reply(self, messages: list[AIMessage | HumanMessage]) -> AIMessage:
        chat_messages = [SystemMessage(message_template)] + messages

        response = self._llm.invoke(chat_messages)

        return response