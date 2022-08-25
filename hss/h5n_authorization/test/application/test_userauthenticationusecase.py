import unittest
from application.userauthenticationusecase import UserAuthenticationUsecase
from application.userauthenticationinputport import UserAuthenticationInputport

from application.userdata import UserData
from application.tokendata import TokenData
from factory.authenticationfactory import AuthenticationFactory #Interface
from factory.userauthenticationinputportfactory import UserAuthenticationInputportFactory
from factory.userauthenticationinputportfactoryimpl import UserAuthenticationInputportFactoryImpl

class TestUserAuthenticationUsecase(unittest.TestCase):
    userauthenticationinputportfactory: UserAuthenticationInputportFactory = UserAuthenticationInputportFactoryImpl()
    userauthenticationusecase: UserAuthenticationInputport = userauthenticationinputportfactory.create_authentication_inputport()

    def test_authentication_success(self):
        userdata: UserData = UserData("horizon", "Halcyon441")
        token: TokenData = self.userauthenticationusecase.handle_userdata(userdata)
        self.assertIsNotNone(token.token)
        self.assertIsNotNone(token.expiration_date)
        #print("token: {} expiration: {}".format(token.token, token.expiration_date))

    def test_authentication_invalid_user_id(self):
        userdata: UserData = UserData("nothorizon", "Halcyon441")
        with self.assertRaises(Exception):
            token: TokenData = self.userauthenticationusecase.handle_userdata(userdata)

    def test_authentication_invalid_password(self):
        userdata: UserData = UserData("horizon", "notHalcyon441")
        with self.assertRaises(Exception):
            token: TokenData = self.userauthenticationusecase.handle_userdata(userdata)

if __name__ == "__main__":
    unittest.main()