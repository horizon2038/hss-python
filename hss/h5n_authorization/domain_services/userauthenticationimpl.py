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
        if not (self.__check_user_data(id, hashed_password)):
            print ("failed authenticate")
            raise Exception

        return self.__create_user(id, hashed_password)

    def __check_user_data(self, id: Id, hashed_password: HashedPassword) -> bool:
        if not (self.__exists_user(id)):
            print("This user ID does not exist")
            raise Exception

        correct_password: HashedPassword = self.__generate_correct_password(id)

        if not (self.__equals_user(correct_password, hashed_password)):
            print("Value not equal")
            raise Exception

        return True

    def __exists_user(self, id: Id) -> bool:
        target_id: str = id.get_id()
        return self.userrepository.userexists(target_id)

    def __generate_correct_password(self, id: Id) -> HashedPassword:
        correct_password: HashedPassword = self.__searchpassword_byuserid(id.get_id())
        return HashedPassword(correct_password)

    def __searchpassword_byuserid(self, id: str) -> str:
        return self.userrepository.searchpassword_byuserid(id)

    def __equals_user(self, correct_password: HashedPassword, hashed_password: HashedPassword) -> bool:
        return correct_password.equals(hashed_password)

    def __create_user(self, id: Id, hashed_password: HashedPassword) -> User:
        token: Token = self.__generate_token()
        return self.userfactory.createuser(id, hashed_password, token)

    def __generate_token(self) -> Token:
        token: Token = self.tokengenerator.generate_token()
        return token
