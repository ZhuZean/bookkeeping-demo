from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from main import app
from app.db.models import base_model
from app.db.session import engine, SessionLocal
from app.tests.fixtures.bill import *


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="function")
def db() -> Generator:
    try:
        base_model.BASE.metadata.create_all(engine)
        yield SessionLocal()
    finally:
        SessionLocal().close_all()
        engine.dispose()
        base_model.BASE.metadata.drop_all(engine)
