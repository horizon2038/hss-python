import hashlib

from domain.user import User #Interface

from domain.id import Id
from domain.password import Password
from domain.token import Token

class UserImpl():
    id: Id
    password: Password
    token: Token

    def __init__(self, id: Id, password: Password, token: Token): #Assertions are already made in the value object
        self.id = id
        self.password = password
        self.token = Token

    def changepassword(self, newpassword: Password):
        self.password = newpassword

if __name__ == "__main__":
    uid = Id("tanaka")
    hashed_password: any = hashlib.sha256("steinsgate".encode()).hexdigest()
    upass = Password(hashed_password)
    user: User = UserImpl(uid, upass)
    print("{0}: {1}".format(user.id.getid(), user.password.getpassword()))

    hashed_password: any = hashlib.sha256("roboticsnotes".encode()).hexdigest()
    newpass = Password(hashed_password)
    user.changepassword(newpass)
    print("{0}: {1}".format(user.id.getid(), user.password.getpassword()))