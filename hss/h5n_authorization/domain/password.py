class Password(): #caution:Unhashed
    def __init__(self, password: str):
        self.__value: str = self.__check_password(password)

    def __check_password(self, password: str):
        if password is None:
            raise Exception("Password is none")
        elif len(password) <= 3:
            raise Exception("Password is out of range")
        else:
            return password

    def get_password(self):
        return self.__value

    def equals(self, target_password: 'Password'):
        return self.get_password() == target_password.get_password()