from typing import Optional
from enum import Enum
from decimal import Decimal
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel
from app.db.models.bill import BillTypeEnum


class BaseBill(BaseModel):
    bill_type: BillTypeEnum
    note: str
    price: Decimal
    payment_id: UUID
    usage_id: UUID
    currency_id: UUID

    class Config:
        orm_mode = True


class BillCreate(BaseBill):
    pass


class BillUpdate(BaseBill):
    pass
