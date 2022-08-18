from typing import Protocol

class TokenGenerator():
    def generatetoken(self):
        pass

import secrets

class TokenGeneratorImpl():
    def __init__(self):
        pass

    def generatetoken(self):
        return secrets.token_hex()