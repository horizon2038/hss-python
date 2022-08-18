from typing import Protocol

from userdata import UserData
from user import Id, Password, User, UserImpl

class UserFactory():
    def __init__(self):
        pass

    def createuser(userdata: UserData):
        user: User = UserImpl(userdata.id, userdata.password)
        return user