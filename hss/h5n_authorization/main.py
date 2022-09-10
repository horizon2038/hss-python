from application.userauthenticationinputport import UserAuthenticationInputport
from infrastructure.app import ServerCore
from factory.userauthenticationinputportfactoryimpl import UserAuthenticationInputportFactoryImpl

if __name__ == "__main__":
    print("running horizon hss-authorization")
    user_authentication_usecase: UserAuthenticationInputport = UserAuthenticationInputportFactoryImpl().create_authentication_inputport()
    authorization_server: ServerCore = ServerCore(user_authentication_usecase)
    authorization_server.run()
