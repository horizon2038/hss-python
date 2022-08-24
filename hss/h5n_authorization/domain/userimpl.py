from domain.user import User #Interface

from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token

class UserImpl():
    id: Id
    hashed_password: HashedPassword
    token: Token

    def __init__(self, id: Id, hashed_password: HashedPassword, token: Token): #Assertions are already made in the value object
        self.id = id
        self.hashed_password = hashed_password
        self.token = token

    def get_id(self) -> Id:
        return self.id
        
    def get_token(self) -> Token:
        return self.token

    def changepassword(self, new_hashed_password: HashedPassword):
        self.password = new_hashed_password