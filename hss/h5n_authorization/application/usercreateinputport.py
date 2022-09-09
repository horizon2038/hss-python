from typing import Protocol

from application.userdata import UserData
from application.tokendata import TokenData

class UserCreateInputport(Protocol):
    def authenticate(userdata: UserData) -> TokenData:
        pass
