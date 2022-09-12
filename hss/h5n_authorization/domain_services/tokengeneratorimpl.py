import secrets
import time
from xmlrpc.client import DateTime

from domain.token import Token
from domain_services.tokengenerator import TokenGenerator #Interface

class TokenGeneratorImpl():
    def __init__(self):
        pass

    def generate_token(self) -> Token:
        hextoken: str = secrets.token_hex()
        now: int = int(time.time())
        expiration_amount: int = 2592000 #30 days
        expires_in = now + expiration_amount
        return Token(hextoken, expires_in)
