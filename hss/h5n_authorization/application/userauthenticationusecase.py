from domain.passwordhashgenerator import PasswordHashGenerator
from domain.tokengenerator import TokenGenerator
from application.userrepository import UserRepository
from application.userdata import UserData

class UserAuthenticationUsecase():
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