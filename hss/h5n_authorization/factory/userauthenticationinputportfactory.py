from typing import Protocol
from application.userauthenticationinputport import UserAuthenticationInputport

class UserAuthenticationInputportFactory(Protocol):
    def __init__(self):
        pass

    def create_authentication_inputport(self) -> UserAuthenticationInputport:
        pass