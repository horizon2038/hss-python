from userrepository import UserRepository
from userinputport import UserData
from passwordhashgenerator import PasswordHashGenerator, PasswordHashGeneratorImpl
from tokengenerator import TokenGenerator, TokenGeneratorImpl

from userrepositoryimpl import UserRepositoryMySQL
    
class UserCleateImpl():
    def __init__(self, userreposiory: UserRepository, passwordhashgenerator: PasswordHashGenerator):
        self.userrepository = userreposiory
        self.passwordhashgenerator: PasswordHashGenerator = passwordhashgenerator

    def handleuserdata(self, userdata: UserData):
        hashed_password: str = self.passwordhashgenerator.generatehash(userdata.password)
        self.userrepository.adduser(userdata.id, hashed_password)

class UserAuthenticationImpl():
    def __init__(self, userrepository: UserRepository, passwordhashgenerator: PasswordHashGenerator, tokengenerator: TokenGenerator):
        self.userrepository = userrepository
        self.passwordhashgenerator: PasswordHashGenerator = passwordhashgenerator
        self.tokengenerator: TokenGenerator = tokengenerator

    def handleuserdata(self, userdata: UserData):
        if (self.userrepository.userexists(userdata.id)):
            hashed_password: str = self.userrepository.searchpassword_byuserid(userdata.id)
            target_password: str = self.passwordhashgenerator.generatehash(userdata.password)
            if(hashed_password == target_password):
                return self.tokengenerator.generatetoken()
            else:
                return
        else:
            return
            

if __name__ == "__main__":
    UCI = UserCleateImpl(UserRepositoryMySQL(), PasswordHashGeneratorImpl())
    UAI = UserAuthenticationImpl(UserRepositoryMySQL(), PasswordHashGeneratorImpl(), TokenGeneratorImpl())
    userdata: UserData = UserData("testuser","testpassword")
    print(UAI.handleuserdata(userdata))
