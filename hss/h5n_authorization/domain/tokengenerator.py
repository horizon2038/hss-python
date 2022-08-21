from typing import Protocol

class TokenGenerator(Protocol):
    def generatetoken(self):
        pass