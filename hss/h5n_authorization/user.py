"""
 Copyright (c) 2022 horizon2038

 Permission is hereby granted, free of charge, to any person obtaining a copy of
 this software and associated documentation files (the "Software"), to deal in
 the Software without restriction, including without limitation the rights to
 use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 the Software, and to permit persons to whom the Software is furnished to do so,
 subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 """
from typing import Protocol
import hashlib

class Id():
    def __init__(self, id: str):
        self.__value: str = self.__checkid(id)

    def __checkid(self, id: str):
        if id is None:
            raise Exception
        elif len(id) <= 3:
            raise Exception
        else:
            return id

    def getid(self):
        return self.__value

    def equals(self, targetid: 'Id'):
        if self.__value == targetid.__value:
            return True
        else:
            return False

class Password():
    def __init__(self, password: str):
        self.__value: str = self.__checkpassword(password)

    def __checkpassword(self, password: str):
        if password is None:
            raise Exception
        elif len(password) <= 3:
            raise Exception
        else:
            return password

    def getpassword(self):
        return self.__value

    def equals(self, targetpassword: 'Password'):
        if self.__value == targetpassword.__value:
            return True
        else:
            return False

class User(Protocol):
    def __init__(self, id: Id, password: Password):
        pass

class UserImpl():
    id: Id
    password: Password

    def __init__(self, id: Id, password: Password): #Assertions are already made in the value object
        self.id = id
        self.password = password

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