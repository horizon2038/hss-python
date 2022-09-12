from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User
from domain_services.tokengenerator import TokenGenerator
from domain_services.authenticationexception import AuthenticationException
from factory.userfactory import UserFactory

class UserAuthenticationImpl():
    def __init__(self, userfactory: UserFactory, tokengenerator: TokenGenerator):
        #These are injected by the Factory, so there is no problem even if they are redundant.
        self.userfactory: UserFactory = userfactory
        self.tokengenerator: TokenGenerator = tokengenerator

    def authenticate(self, user: User, hashed_password: HashedPassword) -> bool: #already hashed
        self.__check_user_password(user.get_password(), hashed_password)
        self.__update_token(user)
        return True

    def __check_user_password(self, correct_password: HashedPassword, hashed_password: HashedPassword) -> bool:
        if not (correct_password.equals(hashed_password)):
            raise AuthenticationException("Incorrect Password")
        return True

    def __update_token(self, user: User):
        __token: Token = self.tokengenerator.generate_token()
        user.update_token(__token)