from langchain_core.tools import tool

from application.infrastructure.persistance.in_memory_storage import InMemoryStorage


@tool
def add_complaint(email_address: str, order_number: str, complaint_content: str) -> bool:
    """
    Wywołaj, aby dodać nową reklamacje do systemu

    :param email_address: adres e-mail osoby zgłaszającej reklamację
    :param order_number: numer zamówienia, którego dotyczy reklamacja
    :param complaint_content: informacja od użytkownika, która mówi czego tyczy się reklamacja
    :return: zwracana wartość to True albo False, True jak udało się dodać reklamacje, False jak nie
    """
    print("ADD COMLAINT CALLED")

    storage = InMemoryStorage()

    storage.add_new_complaint(complaint_content, order_number, email_address)

    return True
