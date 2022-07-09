from typing import Protocol

class UserData():
    def __init__(self, id: str, password: str):
        self.id = id
        self.password = password

class UserCreate(Protocol):
    def handleuserdata(userdata: UserData):
        pass

class UserAuthentication(Protocol):
    def handleuserdata(userdata: UserData):
        pass
