from userrepository import UserRepository
from userdata import UserData
from domain.passwordhashgenerator import PasswordHashGenerator, PasswordHashGeneratorImpl
from domain.tokengenerator import TokenGenerator, TokenGeneratorImpl

from infrastructure.userrepositoryimpl import UserRepositoryMySQL
    
class UserCleateImpl():
    def __init__(self, userreposiory: UserRepository, passwordhashgenerator: PasswordHashGenerator):
        self.userrepository = userreposiory
        self.passwordhashgenerator: PasswordHashGenerator = passwordhashgenerator

    def handleuserdata(self, userdata: UserData):
        hashed_password: str = self.passwordhashgenerator.generatehash(userdata.password)
        self.userrepository.adduser(userdata.id, hashed_password)