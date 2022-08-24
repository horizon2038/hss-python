from typing import Protocol
from application.userdata import UserData

class UserAuthenticateInputport(Protocol):
    def handle_userdata(userdata: UserData):
        pass