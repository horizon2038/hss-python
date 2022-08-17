from typing import Protocol
class UserRepository(Protocol):
    def userexists(self, id: str):
        pass

    def searchpassword_byuserid(self, id: str) -> str:
        pass

    def changeuserpassword(self, id: str, password: str):
        pass

    def adduser(self, id: str, password: str):
        pass

    def changeuserpassword(self, id: str, password: str):
        pass

    def deleteuser(self, id: str):
        pass
    

