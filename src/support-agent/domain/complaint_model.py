from datetime import datetime

from attr import dataclass


@dataclass
class Complaint:
    status: str
    customer_email: str
    order_number: str
    complaint_context: str
    created_at: datetime
    modified_at: datetime
    comments: str
