from typing import Protocol

from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.user import User

class UserAuthentication(Protocol):
    def __init__(self):
        pass

    def authenticate(self, user: User, hashed_password: HashedPassword) -> bool:
        pass
    
