import unittest
from application.userauthenticationusecase import UserAuthenticationUsecase
from application.userauthenticationinputport import UserAuthenticationInputport

from application.userdata import UserData
from application.tokendata import TokenData
from factory.authenticationfactory import AuthenticationFactory #Interface
from factory.userauthenticationinputportfactory import UserAuthenticationInputportFactory
from factory.userauthenticationinputportfactoryimpl import UserAuthenticationInputportFactoryImpl

class TestUserAuthenticationUsecase(unittest.TestCase):
    def test_authentication(self):
        userauthenticationinputportfactory: UserAuthenticationInputportFactory = UserAuthenticationInputportFactoryImpl()
        userdata: UserData = UserData("horizon", "Halcyon441")
        userauthenticationusecase: UserAuthenticationInputport = userauthenticationinputportfactory.create_authentication_inputport()
        token: TokenData = userauthenticationusecase.handle_userdata(userdata)
        print("token: {} expiration: {}".format(token.token, token.expiration_date))

if __name__ == "__main__":
    unittest.main()