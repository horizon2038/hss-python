from domain.passwordhashgenerator import PasswordHashGenerator
from domain_services.userauthentication import UserAuthentication
from domain.id import Id
from domain.password import Password
from domain.hashedpassword import HashedPassword, hashed_password
from domain.user import User
from application.userrepository import UserRepository
from application.userdata import UserData
from factory.authenticationfactory import AuthenticationFactory

class UserAuthenticationUsecase():
    def __init__(self, userrepository: UserRepository, authenticationfactory: AuthenticationFactory, passwordhashgenerator: PasswordHashGenerator):
        self.userrepository: UserRepository = userrepository
        self.authenticationfactory: AuthenticationFactory = authenticationfactory
        self.passwordhashgenerator: PasswordHashGenerator = passwordhashgenerator

    def handle_userdata(self, userdata: UserData):
        userauthentication: UserAuthentication = self.authenticationfactory.create_authentication()
        id: Id = Id(userdata.id)
        password: Password = Password(userdata.password)
        hashed_password: HashedPassword = PasswordHashGenerator.generate_hash(password)
        user: User = userauthentication.authenticate(id, hashed_password)