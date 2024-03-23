from fastapi import APIRouter
from fastapi import Body
from fastapi import Path
from cryptography.fernet import InvalidToken
from fastapi.responses import JSONResponse
from database.db import content_db

from services import crypt_content


secrets_router = APIRouter()


@secrets_router.post("/{secret_key:str}")
def return_secret(
    secret_key: str = Path(),
    code_phrase: str = Body(min_length=8),
):
    encrypted_content = content_db.get(name=secret_key)
    if not encrypted_content:
        return JSONResponse(
            status_code=404,
            content={"message": "secret_key not found"},
        )

    try:
        decrypted_content = crypt_content.decrypt_text(
            encrypted_bytes=encrypted_content,
            password=code_phrase,
        )
    except InvalidToken:
        return JSONResponse(
            status_code=404,
            content={"message": "secret_key not found"},
        )

    # deleting redis keys
    content_db.delete(secret_key)

    return decrypted_content
