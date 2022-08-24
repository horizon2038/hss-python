from typing import Protocol
from domain.password import Password
from domain.hashedpassword import HashedPassword

class PasswordHashGenerator(Protocol):
    def generate_hash(self, password: Password) -> HashedPassword:
        pass