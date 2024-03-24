from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from cryptography.fernet import Fernet

# Функция для создания ключа из пароля
def create_key_from_password(password: str, salt_bytes: bytes) -> bytes:
    password_bytes = password.encode() # Конвертируем пароль в тип bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_bytes,
        iterations=100_000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key

# Функция для шифрования текста
def encrypt_message(message: str, password: str, salt_bytes: bytes) -> bytes:
    key = create_key_from_password(password, salt_bytes)
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode('utf-8'))
    return encrypted_message

# Функция для расшифровки текста
def decrypt_message(encrypted_message: bytes, password: str, salt_bytes: bytes) -> str:
    key = create_key_from_password(password, salt_bytes)
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode('utf-8')
    return decrypted_message