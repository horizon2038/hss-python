import asyncio

from application.userauthenticationinputport import UserAuthenticationInputport
from infrastructure.app import ServerCore
from factory.userauthenticationinputportfactoryimpl import UserAuthenticationInputportFactoryImpl

async def main():
    init()
    user_authentication_usecase: UserAuthenticationInputport = UserAuthenticationInputportFactoryImpl().create_authentication_inputport()
    authorization_server: ServerCore = ServerCore(user_authentication_usecase)
    authorization_server.run()

def init():
    print("\033[05;44m" + "horizon Server Suite: Authorization" + "\033[0m")

if __name__ == "__main__":
    asyncio.run(main())