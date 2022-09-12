from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User

class UserFactory:
    def __init__(self):
        pass

    def createuser(self, id: Id, hashed_password: HashedPassword, token: Token) -> User:
        pass