from userdata import UserData
from userrepository import UserRepository
from tokengenerator import TokenGenerator
from userfactory import UserFactory

class UserAuthentication():
    def __init__(self, userfactory: UserFactory, userrepository: UserRepository, tokengenerator: TokenGenerator):
        #These are injected by the Factory, so there is no problem even if they are redundant.
        self.userfactory: UserFactory = userfactory
        self.userrepository: UserRepository = userrepository
        self.tokengenerator: TokenGenerator = tokengenerator

    def authenticate(self, userdata: UserData): #already hashed
        if (self.userrepository.userexists(userdata.id)):
            correct_password: str = self.userrepository.searchpassword_byuserid(userdata.id)
            if(userdata.password == correct_password):
                user = self.userfactory.createuser(userdata.id, userdata.password)
                return user

    def __generatetoken(self, password: str):
        return self.tokengenerator.generatetoken(password)

    
