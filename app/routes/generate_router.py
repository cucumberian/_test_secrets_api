import os

from services import crypt_content
from database.db import content_db

from fastapi import APIRouter
from fastapi import Body
from fastapi.responses import JSONResponse

generate_router = APIRouter()


@generate_router.post("")
def get_secret_key(
    secret_content: str = Body(
        min_length=1, title="secret content, min_length=1"
    ),
    code_phrase: str = Body(
        min_length=8,
        title="code phrase, min_length=8",
    ),
    ttl_seconds: int = Body(
        3600,
        ge=5,
        le=3600,
        title="time to live in seconds, default=3600s",
    ),
):
    crypted_content: bytes = crypt_content.encrypt_text(
        text=secret_content,
        password=code_phrase,
    )
    # random key generation
    rand_key = os.urandom(32).hex()

    result = content_db.set(
        name=rand_key,
        value=crypted_content,
        ex=ttl_seconds,
    )
    if not result:
        return JSONResponse(
            status_code=500,
            content={"message": "Something went wrong!"},
        )
    return rand_key
