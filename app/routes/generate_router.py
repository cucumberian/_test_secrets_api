import os

from services import crypt_content
from database.db import content_db

from fastapi import APIRouter
from fastapi import Body
from fastapi.responses import JSONResponse

from config import Config
from models.models import SecretGenerate
from models.models import SecretGenerateResponse

generate_router = APIRouter()

salt_bytes = Config.SALT.encode()


@generate_router.post(
    "",
    response_model=SecretGenerateResponse,
    tags=["generate"],
)
def get_secret_key(
    secret_generate: SecretGenerate = Body(),
):
    encrypted_content: bytes = crypt_content.encrypt_message(
        message=secret_generate.secret_content,
        password=secret_generate.code_phrase,
        salt_bytes=salt_bytes,
    )
    # random key generation
    rand_key = os.urandom(Config.KEY_SIZE).hex()

    result = content_db.set(
        name=rand_key,
        value=encrypted_content,
        ex=secret_generate.ttl_seconds,
    )

    response = SecretGenerateResponse(
        secret_key=rand_key,
        ttl_seconds=secret_generate.ttl_seconds,
    )

    if not result:
        return JSONResponse(
            status_code=500,
            content={"message": "Something went wrong!"},
        )
    return response
