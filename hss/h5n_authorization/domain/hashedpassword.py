class HashedPassword():
    def __init__(self, hashed_password: str):
        self.__value: str = self.__check_password(hashed_password)

    def __check_password(self, hashed_password: str):
        if hashed_password is None:
            raise Exception
        elif len(hashed_password) <= 3:
            raise Exception
        else:
            return hashed_password

    def get_password(self):
        return self.__value

    def equals(self, target_password: 'HashedPassword'):
        if self.__value == target_password.__value:
            return True
        else:
            return False