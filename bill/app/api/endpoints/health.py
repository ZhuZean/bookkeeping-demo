from typing import Any
from fastapi import APIRouter,  Response

router = APIRouter()

@router.get('/')
def get_health() -> Any:
    return Response(content="Alive and well!", media_type="text/plain")
