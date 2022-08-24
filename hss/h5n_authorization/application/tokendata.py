class TokenData:
    def __init__(self, token: str, expiration_date: int):
        self.token: str = token
        self.expiration_date: int = expiration_date