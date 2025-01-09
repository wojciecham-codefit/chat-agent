from langchain_core.tools import tool

from application.infrastructure.persistance.in_memory_storage import InMemoryStorage


@tool
def check_complaint(order_number: str) -> str:
    """
    Wywołaj,a by sprawdzi stan reklamacj po numerze zamówienia

    :param order_number: numer zamówienia, którego dotyczyła reklamacja
    :return: zwraca informację o statusie reklamacji w formie tekstu
    """
    print("CHECK COMLAINT CALLED")

    storage = InMemoryStorage()

    complaint = storage.get_complaint_by_order_number(order_number)

    if complaint is None:
        return "Nie ma żadnej reklamacji dla tego zamówienia"

    return f'Stan reklamacji: {complaint.status}, ostatnia modyfikacja: {complaint.modified_at.strftime("%m/%d/%Y, %H:%M:%S")}, uwagi obsługi sklepu: {complaint.comments}'