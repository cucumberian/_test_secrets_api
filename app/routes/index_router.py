from fastapi import APIRouter
from .generate_router import generate_router
from .secrets_router import secrets_router

index_router = APIRouter()

index_router.include_router(prefix="/generate", router=generate_router)
index_router.include_router(prefix="/secrets", router=secrets_router)
