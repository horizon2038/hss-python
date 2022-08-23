import secrets
import time
from xmlrpc.client import DateTime

from domain.tokengenerator import TokenGenerator #Interface
from domain.token import Token

class TokenGeneratorImpl():
    def __init__(self):
        pass

    def generate_token(self) -> Token:
        hextoken: str = secrets.token_hex()
        now: int = int(time.time())
        expiration_amount: int = 2592000
        expiration_date = now + expiration_amount
        return Token(hextoken, expiration_date)