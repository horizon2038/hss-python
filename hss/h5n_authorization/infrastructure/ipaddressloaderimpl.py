import socket

class IPAddressLoaderImpl():
    def __init__(self) -> None:
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def load_ip_address(self) -> str:
        __ip_address: str = socket.gethostbyname(socket.gethostname())
        return __ip_address