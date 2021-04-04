from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class BasePayment(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True


class PaymentCreate(BasePayment):
    pass


class PaymentUpdate(BasePayment):
    pass
