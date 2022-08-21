from typing import Protocol

class PasswordHashGenerator(Protocol):
    def generatehash(self, password: str):
        pass

