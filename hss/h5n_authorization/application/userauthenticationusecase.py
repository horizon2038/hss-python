from domain.id import Id
from domain.password import Password
from domain.hashedpassword import HashedPassword
from domain.user import User
from domain.token import Token
from domain_services.passwordhashgenerator import PasswordHashGenerator
from domain_services.userauthentication import UserAuthentication
from domain_services.authenticationexception import AuthenticationException
from application.userrepository import UserRepository
from application.userdata import UserData
from application.tokendata import TokenData
from application.applicationexception import ApplicationException
from factory.authenticationfactory import AuthenticationFactory

class UserAuthenticationUsecase():
    def __init__(self, userrepository: UserRepository, authenticationfactory: AuthenticationFactory, passwordhashgenerator: PasswordHashGenerator):
        self.userrepository: UserRepository = userrepository
        self.authenticationfactory: AuthenticationFactory = authenticationfactory
        self.passwordhashgenerator: PasswordHashGenerator = passwordhashgenerator
        self.userauthentication: UserAuthentication = self.authenticationfactory.create_authentication()

    def authenticate(self, userdata: UserData) -> TokenData:
        try:
            user: User = self.__create_user(userdata) #TODO: ID, Password, Token Exception -> wrap authentication exception
            token: Token = user.get_token() #OK
            tokendata: TokenData = self.__create_tokendata(token)
            return tokendata
        except AuthenticationException as e:
            raise ApplicationException(str(e))
        finally:
            pass

    def __create_user(self, userdata: UserData) -> User:
        id: Id = Id(userdata.id)
        hashed_password: HashedPassword = self.__create_hashed_password(userdata.password)
        return self.userauthentication.authenticate(id, hashed_password)
    
    def __create_hashed_password(self, password: str) -> HashedPassword:
        password: Password = Password(password)
        return self.passwordhashgenerator.generate_hash(password)

    def __create_tokendata(self, token: Token) -> TokenData:
        tokendata: TokenData = TokenData(token.get_token(), token.get_expiration_date())
        return tokendata