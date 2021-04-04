#!/usr/bin/python
import uvicorn
from fastapi import APIRouter, FastAPI

from app.core.config import settings
from app.api.endpoints import health, bill


api_router = APIRouter()
api_router.include_router(
    health.router
)
api_router.include_router(
    bill.router, prefix=f'{settings.api_base_path}', tags=['bill']
)

app = FastAPI(docs_url=f'{settings.api_base_path}/docs', openapi_url=f'{settings.api_base_path}/openapi.json')
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
