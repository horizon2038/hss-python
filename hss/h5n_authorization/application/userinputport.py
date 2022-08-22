from typing import Protocol

from application.userdata import UserData

class UserCreate(Protocol):
    def handleuserdata(userdata: UserData):
        pass

class UserAuthenticate(Protocol):
    def handleuserdata(userdata: UserData):
        pass
