class Password(): #caution:Unhashed
    def __init__(self, password: str):
        self.__value: str = self.__check_password(password)

    def __check_password(self, password: str):
        if password is None:
            raise Exception
        elif len(password) <= 3:
            raise Exception
        else:
            return password

    def get_password(self):
        return self.__value

    def equals(self, target_password: 'Password'):
        if self.__value == target_password.__value:
            return True
        else:
            return False