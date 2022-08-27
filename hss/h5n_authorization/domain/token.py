class Token():
    def __init__(self, token: str, expiration_date: int): #expiration date is Epoch time
        self.__token = self.__check_token(token)
        self.__expiration_date = self.__check_expiration_date(expiration_date)

    def get_token(self):
        return self.__token

    def get_expiration_date(self):
        return self.__expiration_date

    def __check_token(self, token: str):
        if token is None:
            raise Exception("Token is none")
        elif len(token) <= 3:
            raise Exception("Token is out of range")
        else:
            return token

    def __check_expiration_date(self, expiration_date: int):
        if expiration_date is None:
            raise Exception("ExpirationDate is none")
        else:
            return expiration_date