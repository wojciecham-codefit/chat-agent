from datetime import datetime

from domain.complaint_model import Complaint
from typing import List


class InMemoryStorage:
    complaints: List[Complaint] = []

    def add_new_complaint(self, content: str, order_number: str, email_address: str) -> None:
        now = datetime.now()

        new_complaint = Complaint(
            status='stworzona',
            customer_email=email_address,
            order_number=order_number,
            complaint_context=content,
            created_at=now,
            modified_at=now,
            comments=''
        )

        self.complaints.append(new_complaint)

    def get_complaint_by_order_number(self, order_number: str) -> Complaint | None:
        complaint = next((c for c in self.complaints if c.order_number == order_number))

        return complaint
