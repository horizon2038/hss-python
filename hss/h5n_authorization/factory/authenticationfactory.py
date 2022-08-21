from typing import Protocol

from userdata import UserData
from user import Id, Password, User, UserImpl
from userauthentication import UserAuthentication, UserAuthenticationImpl
from application.userrepository import UserRepository
from infrastructure.userrepositoryimpl import UserRepositoryMySQL
from domain.tokengenerator import TokenGenerator

class AuthenticationFactory():
    def __init__(self):
        pass

class AuthenticationFactoryImpl():
    def __init__(self):
        pass

    def createuser(userdata: UserData):
        user: User = UserImpl(userdata.id, userdata.password)
        return user

    def createauthentication():
        userauthentication: UserAuthentication = UserAuthenticationImpl(UserRepository, TokenGenerator)
        return userauthentication