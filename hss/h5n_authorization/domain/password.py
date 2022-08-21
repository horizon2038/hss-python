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