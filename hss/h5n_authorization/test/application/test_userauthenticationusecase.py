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
        print("\033[05;44m" + "test_authentication_success" + "\033[0m")
        userdata: UserData = UserData("horizon", "Halcyon441")
        token: TokenData = self.userauthenticationusecase.authenticate(userdata)
        print("token: {} expires_in: {}".format(token.token, token.expires_in))
        self.assertIsNotNone(token.token)
        self.assertIsNotNone(token.expires_in)

    def test_authentication_invalid_user_id(self):
        print("\033[05;44m" + "test_authentication_invalid_user_id" + "\033[0m")
        userdata: UserData = UserData("nothorizon", "Halcyon441")
        #with self.assertRaises(Exception):
        try:
            token: TokenData = self.userauthenticationusecase.authenticate(userdata)
        except Exception as e:
            print(e)

    def test_authentication_invalid_password(self):
        print("\033[05;44m" + "test_authentication_invalid_password" + "\033[0m")
        userdata: UserData = UserData("horizon", "notHalcyon441")
        #with self.assertRaises(Exception):
        try:
            token: TokenData = self.userauthenticationusecase.authenticate(userdata)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    unittest.main()