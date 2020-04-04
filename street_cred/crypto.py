import os

from cryptography.fernet import Fernet, MultiFernet


class NullFernet:
    """
    A "Null" encryptor class that doesn't encrypt or decrypt but that presents
    a similar interface to Fernet.
    The purpose of this is to make the rest of the code not have to know the
    difference, and to only display the message once, not 20 times when
    `airflow db init` is ran.
    """
    is_encrypted = False

    def decrypt(self, b):
        return b

    def encrypt(self, b):
        return b


_fernet = None  # type: Optional[FernetProtocol]


def get_fernet():
    """Get fernet encrypter."""
    global _fernet

    if _fernet:
        return _fernet

    fernet_key = os.getenv('FERNET_KEY')
    if not fernet_key:
        _fernet = NullFernet()
    else:
        _fernet = MultiFernet([
            Fernet(fernet_part.encode('utf-8'))
            for fernet_part in fernet_key.split(',')
        ])
        _fernet.is_encrypted = True
    return _fernet
