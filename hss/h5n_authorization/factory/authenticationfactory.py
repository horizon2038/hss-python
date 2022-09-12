from typing import Protocol

from domain_services.userauthentication import UserAuthentication

class AuthenticationFactory(Protocol):
    def __init__(self):
        pass

    def create_authentication(self) -> UserAuthentication:
        pass