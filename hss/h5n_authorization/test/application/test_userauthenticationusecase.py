import unittest
from application.userauthenticationusecase import UserAuthenticationUsecase
from application.userauthenticationinputport import UserAuthenticationInputport

from domain.id import Id
from domain.password import Password
from domain.hashedpassword import HashedPassword
from domain.user import User
from domain.token import Token
from domain_services.passwordhashgenerator import PasswordHashGenerator
from domain_services.userauthentication import UserAuthentication
from application.userrepository import UserRepository
from application.userdata import UserData
from application.tokendata import TokenData
from factory.authenticationfactory import AuthenticationFactory
from factory.userauthenticationinputportfactoryimpl import UserAuthenticationInputportFactoryImpl

class TestUserAuthenticationUsecase(unittest.TestCase):
    def test_authentication(self):
        userauthenticationinputportfactory = UserAuthenticationInputportFactoryImpl()
        userdata: UserData = UserData("horizon", "Halcyon441")
        userauthenticationusecase: UserAuthenticationInputport = userauthenticationinputportfactory.create_authentication_inputport()
        token: TokenData = userauthenticationusecase.handle_userdata(userdata)
        print(token.token, token.expiration_date)


if __name__ == "__main__":
    unittest.main()