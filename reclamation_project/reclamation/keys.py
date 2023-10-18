import secrets

from cryptography import fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from reclamation_app import settings


def chiffrage_msg(msg, key=settings.key, vector_inis=settings.vector_inis):
    algorithm = algorithms.AES(key)
    mode = modes.CTR(vector_inis)
    cipher = Cipher(algorithm, mode)
    encryptor = cipher.encryptor()
    message_encrypted = encryptor.update(msg.encode()) + encryptor.finalize()

    return message_encrypted.decode()


def dechiffrage_msg(msg, key=settings.key, vector_inis=settings.vector_inis):
    algorithm = algorithms.AES(key)
    mode = modes.CTR(vector_inis)
    cipher = Cipher(algorithm, mode)

    decryptor = cipher.decryptor()
    message_decrypted = decryptor.update(msg.encode()) + decryptor.finalize()

    return message_decrypted.decode()


def encrypt(cleartext):
    key = settings.ENCRYPT_KEY
    f = fernet.Fernet(key)
    return f.encrypt(cleartext.encode()).decode()


def decrypt(ciphertext):
    key = settings.ENCRYPT_KEY
    f = fernet.Fernet(key)
    return f.decrypt(ciphertext.encode()).decode()
