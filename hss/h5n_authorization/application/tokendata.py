class TokenData:
    def __init__(self, token: str, expires_in: int):
        self.token: str = token
        self.expires_in: int = expires_in