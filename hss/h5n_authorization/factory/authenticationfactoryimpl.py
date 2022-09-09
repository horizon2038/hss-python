from domain.tokengeneratorimpl import TokenGeneratorImpl
from domain_services.userauthentication import UserAuthentication
from domain_services.userauthenticationimpl import UserAuthenticationImpl
from infrastructure.userrepositoryimpl import UserRepositoryMySQL
from factory.userfactoryimpl import UserFactoryImpl
from factory.authenticationfactory import AuthenticationFactory

class AuthenticationFactoryImpl():
    def __init__(self):
        pass

    def create_authentication(self) -> UserAuthentication:
        userauthentication: UserAuthentication = UserAuthenticationImpl(UserFactoryImpl(), TokenGeneratorImpl())
        print("AuthenticationFactory: Create UserAuthenticationImpl")
        return userauthentication