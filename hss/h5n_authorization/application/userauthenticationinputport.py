from typing import Protocol
from application.userdata import UserData
from application.tokendata import TokenData

class UserAuthenticationInputport(Protocol):
    def handle_userdata(userdata: UserData) -> TokenData:
        pass