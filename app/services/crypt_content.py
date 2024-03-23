import base64
import hashlib
from cryptography.fernet import Fernet


def encrypt_text(text: str, password: str) -> bytes:
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()[:32]
    key = base64.urlsafe_b64encode(password_hash.encode("utf-8"))
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode("utf-8"))
    return encrypted_text


def decrypt_text(encrypted_bytes: bytes, password: str) -> str:
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()[:32]
    key = base64.urlsafe_b64encode(password_hash.encode("utf-8"))
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_bytes)
    return decrypted_text.decode("utf-8")
