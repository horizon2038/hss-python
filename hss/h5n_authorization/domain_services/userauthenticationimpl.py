import secrets

from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User
from domain.tokengenerator import TokenGenerator
from application.userrepository import UserRepository
from factory.userfactory import UserFactory

class UserAuthenticationImpl():
    def __init__(self, userrepository: UserRepository, userfactory: UserFactory, tokengenerator: TokenGenerator):
        #These are injected by the Factory, so there is no problem even if they are redundant.
        self.userrepository: UserRepository = userrepository
        self.userfactory: UserFactory = userfactory
        self.tokengenerator: TokenGenerator = tokengenerator

    def authenticate(self, id: Id, hashed_password: HashedPassword) -> User: #already hashed
        if (self.userrepository.userexists(id)):
            correct_password: HashedPassword = HashedPassword(self.userrepository.searchpassword_byuserid(id))
            if(correct_password.equals(hashed_password)):  
                token: Token = self.__generatetoken()
                return self.userfactory.createuser(id, hashed_password, token)

    def __generatetoken(self) -> Token:
        return self.tokengenerator.generate_token()
