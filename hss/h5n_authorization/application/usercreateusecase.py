from userrepository import UserRepository
from userdata import UserData
from domain.id import Id
from domain.password import Password
from domain.hashedpassword import HashedPassword
from domain_services.passwordhashgenerator import PasswordHashGenerator

from infrastructure.userrepositoryimpl import UserRepositoryMySQL
    
class UserCleateImpl():
    def __init__(self, userreposiory: UserRepository, passwordhashgenerator: PasswordHashGenerator):
        self.userrepository = userreposiory
        self.passwordhashgenerator: PasswordHashGenerator = passwordhashgenerator

    def handle_userdata(self, userdata: UserData):
        password: Password = Password(userdata.password)
        hashed_password: HashedPassword = self.passwordhashgenerator.generate_hash(password)
        self.userrepository.adduser(userdata.id, hashed_password)