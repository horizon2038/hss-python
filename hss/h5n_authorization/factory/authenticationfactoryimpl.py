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
        userauthentication: UserAuthentication = UserAuthenticationImpl(UserRepositoryMySQL(), UserFactoryImpl(), TokenGeneratorImpl())
        return userauthentication

if __name__ == "__main__":
    authenticationfactory: AuthenticationFactory = AuthenticationFactoryImpl()
    userauthentication: UserAuthentication = authenticationfactory.create_authentication()