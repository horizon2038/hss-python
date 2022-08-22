import secrets


from domain.tokengenerator import TokenGenerator #Interface

class TokenGeneratorImpl():
    def __init__(self):
        pass

    def generatetoken(self):
        return secrets.token_hex()