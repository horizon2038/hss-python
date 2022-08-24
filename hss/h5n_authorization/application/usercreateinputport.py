from typing import Protocol

from application.userdata import UserData

class UserCreateInputport(Protocol):
    def handle_userdata(userdata: UserData):
        pass
