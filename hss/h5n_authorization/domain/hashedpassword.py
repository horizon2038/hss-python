class HashedPassword():
    def __init__(self, hashed_password: str):
        self.__value: str = self.__check_password(hashed_password)

    def __check_password(self, hashed_password: str):
        if hashed_password is None:
            raise Exception("HashedPassword is none")
        elif len(hashed_password) <= 3:
            raise Exception("HashedPassword is out of range")
        else:
            return hashed_password

    def get_password(self):
        return self.__value

    def equals(self, target_password: 'HashedPassword') -> bool:
        return self.get_password() == target_password.get_password()