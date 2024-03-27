from pydantic import BaseModel
from pydantic import Field

from config import Config

class SecretAccess(BaseModel):
    code_phrase: str = Field(min_length=Config.CODE_PHRASE_MIN_LENGTH)

class SecretGenerate(SecretAccess):
    secret_content: str = Field(
        min_length=1,
        title="Secret content",
    )
    ttl_seconds: int = Field(
        default=3600,
        ge=5,
        le=7 * 24 * 3600,
        title="time to live in seconds, default=3600s",
    )

class SecretGenerateResponse(BaseModel):
    secret_key: str = Field(
        min_length=Config.KEY_SIZE,
        title="Secret key",
    )
    ttl_seconds: int = Field(title="time to live in seconds")