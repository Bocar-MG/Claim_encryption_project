import secrets

from cryptography import fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from reclamation_app import settings


def chiffrage_msg(msg, key=settings.key, vector_inis=settings.vector_inis):
    msg = msg.encode()
    algorithm = algorithms.AES(key)
    mode = modes.CTR(vector_inis)
    cipher = Cipher(algorithm, mode)
    encryptor = cipher.encryptor()
    message_encrypted = encryptor.update(msg) + encryptor.finalize()

    return message_encrypted


def dechiffrage_msg(msg, key=settings.key, vector_inis=settings.vector_inis):
    algorithm = algorithms.AES(key)
    mode = modes.CTR(vector_inis)
    cipher = Cipher(algorithm, mode)

    decryptor = cipher.decryptor()
    message_decrypted = decryptor.update(msg) + decryptor.finalize()
    message_decrypted1 = message_decrypted.decode()
    return message_decrypted.decode("utf-8")


def encrypt(cleartext):
    key = settings.ENCRYPT_KEY
    f = fernet.Fernet(key)
    return f.encrypt(cleartext.encode()).decode()


def decrypt(ciphertext):
    key = settings.ENCRYPT_KEY
    f = fernet.Fernet(key)
    return f.decrypt(ciphertext.encode()).decode()
