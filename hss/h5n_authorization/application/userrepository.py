from typing import Protocol

from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User

class UserRepository(Protocol):
    def exists(self, id: Id) -> bool:
        pass

    def find_password(self, id: Id) -> HashedPassword:
        pass

    def find_token(self, id: Id) -> Token:
        pass

    def add(self, user: User): #Create New User
        pass

    def store(self, user: User): #Updates can only be made from the aggregate.
        pass

    def delete(self, id: Id):
        pass

