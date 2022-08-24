from domain_services.passwordhashgeneratorimpl import PasswordHashGeneratorImpl
from application.userauthenticationinputport import UserAuthenticationInputport
from application.userauthenticationusecase import UserAuthenticationUsecase
from infrastructure.userrepositoryimpl import UserRepositoryMySQL
from factory.authenticationfactoryimpl import AuthenticationFactoryImpl

class UserAuthenticationInputportFactoryImpl:
    def __init__(self):
        pass

    def create_authentication_inputport(self) -> UserAuthenticationInputport:
        userauthenticationinputport: UserAuthenticationInputport = UserAuthenticationUsecase(UserRepositoryMySQL(), AuthenticationFactoryImpl(), PasswordHashGeneratorImpl())
        print("UserAuthenticationInputportFactory: Create UserAuthenticationInputport")
        return userauthenticationinputport