from domain.id import Id
from domain.password import Password
from domain.

class UserFactory:
    def __init__(self):
        pass

    def createuser(userdata: UserData):
        user: User = UserImpl(userdata.id, userdata.password)
        return user