from .models import Credentials


def get_credentials(key: str) -> Credentials:
    return Credentials(conn_id=key)
