from typing import Protocol

from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User
from factory.userfactory import UserFactory

class UserRepository(Protocol):
    def __init__(self, userfactory: UserFactory):
        pass

    def id_exists(self, id: Id) -> bool:
        pass

    def token_exists(self, token: Token) -> bool:
        pass

    def retrieve_user_byid(self, id: Id) -> User:
        pass

    def retrieve_user_bytoken(self, token: Token) -> User:
        pass

    def add(self, user: User): #Create New User
        pass

    def store(self, user: User): #Updates can only be made from the aggregate.
        pass

    def delete(self, id: Id):
        pass

