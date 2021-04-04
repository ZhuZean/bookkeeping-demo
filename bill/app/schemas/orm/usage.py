from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class BaseUsage(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True


class UsageCreate(BaseUsage):
    pass


class UsageUpdate(BaseUsage):
    pass
