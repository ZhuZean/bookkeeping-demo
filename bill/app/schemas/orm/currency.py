from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class BaseCurrency(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True


class CurrencyCreate(BaseCurrency):
    pass


class CurrencyUpdate(BaseCurrency):
    pass
