from typing import Protocol
from userdata import UserData
from userrepository import UserRepository
from tokengenerator import TokenGenerator

class UserAuthentication(Protocol):
    def __init__(self):
        pass

    def authenticate(self, userdata: UserData):
        pass

class UserAuthenticationImpl():
    def __init__(self, userrepository: UserRepository, tokengenerator: TokenGenerator):
        #These are injected by the Factory, so there is no problem even if they are redundant.
        self.userrepository: UserRepository = userrepository
        self.tokengenerator: TokenGenerator = tokengenerator

    def authenticate(self, userdata: UserData): #already hashed
        if (self.userrepository.userexists(userdata.id) and userdata != None):
            correct_password: str = self.userrepository.searchpassword_byuserid(userdata.id)
            if(userdata.password == correct_password):
                return self.__generatetoken()

    def __generatetoken(self):
        return self.tokengenerator.generatetoken()

    
