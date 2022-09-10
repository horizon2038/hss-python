class Token():
    def __init__(self, token: str, expires_in: int): #expiration date is Epoch time
        self.__token = self.__check_token(token)
        self.__expires_in = self.__check_expires_in(expires_in)

    def get_token(self):
        return self.__token

    def get_expires_in(self):
        return self.__expires_in

    def __check_token(self, token: str):
        if token is None:
            raise Exception("Token is none")
        elif len(token) <= 3:
            raise Exception("Token is out of range")
        else:
            return token

    def __check_expires_in(self, expires_in: int):
        if expires_in is None:
            raise Exception("Expires_in is none")
        else:
            return expires_in