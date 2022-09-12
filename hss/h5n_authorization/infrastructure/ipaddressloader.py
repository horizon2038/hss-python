from typing import Protocol

class IPAddressLoader(Protocol):
    def load_ip_address() -> str:
        pass