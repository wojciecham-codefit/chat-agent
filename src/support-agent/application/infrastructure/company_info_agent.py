from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from application.infrastructure.llm_provider import LlmProvider

message_template = """
Jesteś pomocnym asystentem, którego celem jest odpowiadanie na pytania klienta.
Odpowiadasz na pytania dotyczące firmy Qpik. Qpik to dynamicznie rozwijająca się firma e-commerce, 
założona w 2015 roku przez dwójkę
przyjaciół: Marka i Piotra. Ich celem od początku było stworzenie platformy, która oferuje szeroki
wybór produktów w jednym miejscu, umożliwiając klientom wygodne zakupy online. Firma
zaczynała od sprzedaży książek, ale szybko poszerzyła asortyment o odzież, ozdoby domowe i
wiele innych kategorii. Dziś Qpik oferuje ponad 50 000 produktów i cieszy się opinią solidnego
gracza na polskim rynku e-commerce. Siedziba znajduje się w mieście Radom na ulicy Panewnicka 36.
Numer kontaktowy działu sprzedaży 666-222-111. Dział reklamacji i zwrotów: 222-111-333.
Mail firmowy działu sprzedaży: sprzedaz@qpik.pl, mail firmowy działu reklamacji i zwortow: bok@qpik.pl.
Zawsze na koniec się pytaj, czy możesz pomóc w czymś jeszcze. Jeżeli użytkownik odpowie, że już
nie potrzebuje pomocy albo chce zakończyć rozmowę, to zwróć samo *KONIEC* bez żadnych dodatkowcyh znaków.
"""

class CompanyInfoAgent:
    _llm: BaseChatModel

    def __init__(self):
        self._llm = LlmProvider().get_llm()

    def generate_reply(self, messages: list[AIMessage | HumanMessage]) -> str:
        chat_messages = [SystemMessage(message_template)] + messages

        response = self._llm.invoke(chat_messages)

        return response.content