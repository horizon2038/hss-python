from typing import Protocol

class PasswordHashGenerator(Protocol):
    def generate_hash(self, password: str):
        pass