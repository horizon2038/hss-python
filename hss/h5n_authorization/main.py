import asyncio

from application.userauthenticationinputport import UserAuthenticationInputport
from infrastructure.app import ServerCore
from factory.userauthenticationinputportfactoryimpl import UserAuthenticationInputportFactoryImpl
from infrastructure.ipaddressloaderimpl import IPAddressLoaderImpl

async def main():
    init()
    user_authentication_usecase: UserAuthenticationInputport = UserAuthenticationInputportFactoryImpl().create_authentication_inputport()
    ip_address_loader: IPAddressLoaderImpl = IPAddressLoaderImpl()
    authorization_server: ServerCore = ServerCore(user_authentication_usecase, ip_address_loader)
    authorization_server.run()

def init():
    print("\033[05;44m" + "horizon Server Suite: Authorization" + "\033[0m")

if __name__ == "__main__":
    asyncio.run(main())