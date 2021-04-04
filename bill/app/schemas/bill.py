from typing import List
from decimal import Decimal

from pydantic import BaseModel

from app.schemas.orm.bill import BaseBill
from app.schemas.orm.payment import BasePayment
from app.schemas.orm.usage import BaseUsage
from app.schemas.orm.currency import BaseCurrency
from .pagination import PaginationResponse


class CreateBillRequest(BaseBill):
    pass


class CreateBillResponse(BaseBill):
    bill_type: str
    note: str
    price: Decimal
    payment: BasePayment
    usage: BaseUsage
    currency: BaseCurrency


class ListBillResponse(PaginationResponse):
    items: List[CreateBillResponse]

    class Config:
        orm_mode = True


class BillFormInfoResponse(BaseModel):
    payment: List[BasePayment]
    usage: List[BaseUsage]
    currency: List[BaseCurrency]
    bill_type: List[str]

    class Config:
        orm_mode = True


class BaseSummary(BaseModel):
    total_expense: Decimal
    total_income: Decimal


class BasePaymentDetail(BaseModel):
    name: str
    amount: Decimal


class BillSummaryResponse(BaseModel):
    summary: BaseSummary
    payment_detail: List[BasePaymentDetail]

    class Config:
        orm_mode = True
