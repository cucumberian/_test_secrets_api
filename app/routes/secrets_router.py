from fastapi import APIRouter
from fastapi import Body
from fastapi import Path
from cryptography.fernet import InvalidToken
from fastapi.responses import JSONResponse
from database.db import content_db

from services import crypt_content
from config import Config
from models.models import SecretAccess

secrets_router = APIRouter()

salt_bytes = Config.SALT.encode()


@secrets_router.post("/{secret_key:str}")
def return_secret(
    secret_key: str = Path(),
    secret_access: SecretAccess = Body(),
):
    code_phrase = secret_access.code_phrase
    print("secret_key =", secret_key)
    print("code_phrase =", code_phrase)
    encrypted_content = content_db.get(name=secret_key)
    if not encrypted_content:
        return JSONResponse(
            status_code=404,
            content={"message": "secret_key not found"},
        )

    try:
        decrypted_content = crypt_content.decrypt_message(
            encrypted_message=encrypted_content,
            password=code_phrase,
            salt_bytes=salt_bytes,
        )
    except InvalidToken:
        return JSONResponse(
            status_code=404,
            content={"message": "secret_key not found"},
        )

    # deleting redis keys
    content_db.delete(secret_key)

    return decrypted_content
