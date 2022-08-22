class UserFactory:
    def __init__(self):
        pass

    def createuser(userdata: UserData):
        user: User = UserImpl(userdata.id, userdata.password)
        return user