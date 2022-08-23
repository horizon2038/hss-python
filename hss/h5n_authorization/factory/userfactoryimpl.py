from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User
from domain.userimpl import UserImpl

class UserFactoryImpl:
    def __init__(self):
        pass

    def createuser(id: Id, hashed_password: HashedPassword, token: Token) -> User:
        user: User = UserImpl(id, hashed_password, token)
        return user