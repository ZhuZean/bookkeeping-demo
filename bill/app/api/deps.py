from typing import Generator, Callable
from app.db.session import SessionLocal

from app.core.config import settings


def get_bill_business() -> Callable:
    return settings.bill_business()


def get_db_session() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


