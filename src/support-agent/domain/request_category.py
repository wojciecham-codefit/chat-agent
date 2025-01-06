from enum import StrEnum

class RequestCategory(StrEnum):
    COMPLAINT = 'complaint'
    RETURN = 'return'
    PURCHASE = 'purchase'
    OTHER = 'other'

    @staticmethod
    def from_string(text: str):
        if RequestCategory.RETURN in text:
            return RequestCategory.RETURN
        if RequestCategory.COMPLAINT in text:
            return RequestCategory.COMPLAINT
        if RequestCategory.PURCHASE in text:
            return RequestCategory.PURCHASE
        if RequestCategory.OTHER in text:
            return RequestCategory.OTHER

        return None
