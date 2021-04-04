#!/usr/bin/python
import uvicorn
from fastapi import APIRouter, FastAPI

from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
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

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
