class Token():
    def __init__(self, token: str, expirationdate: int): #expiration date is Epoch time
        self.token = token
        self.expirationdate = expirationdate