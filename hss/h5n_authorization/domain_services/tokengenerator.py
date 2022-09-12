from typing import Protocol
from domain.token import Token

class TokenGenerator(Protocol):
    def generate_token(self) -> Token:
        pass