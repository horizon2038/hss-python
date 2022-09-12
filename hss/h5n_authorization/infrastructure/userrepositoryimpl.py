import hashlib
import MySQLdb

from application.userrepository import UserRepository
from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User
from factory.userfactory import UserFactory

class UserRepositoryMySQL(): 
    def __connectDB(self):
        self.connection = MySQLdb.Connect(user='root', passwd='Halcyon441', host='localhost', db='h5nserver')

    def __createcursor(self):
        self.cursor = self.connection.cursor()

    def __init__(self, userfactory: UserFactory):
        self.userfactory = userfactory
        self.__connectDB()
        self.__createcursor()

    def id_exists(self, id: Id) -> bool:
        query: str = "SELECT EXISTS(SELECT id FROM users WHERE id=%s)"
        self.cursor.execute(query, (id.get_id(), ))
        res = self.cursor.fetchone()
        return res[0]

    def token_exists(self, token: str) -> bool:
        query: str = "SELECT EXISTS(SELECT token FROM users WHERE token=%s)"
        self.cursor.execute(query, (token, ))
        res = self.cursor.fetchone()
        return res[0]

    def retrieve_user_byid(self, id: Id) -> User:
        query: str = "SELECT id, password, token, expires_in FROM users WHERE id=%s"
        self.cursor.execute(query, (id.get_id(), ))
        res = self.cursor.fetchone()
        __id: Id = Id(res[0])
        __hashed_password: HashedPassword = HashedPassword(res[1])
        __token: Token = Token(res[2], res[3])
        return self.userfactory.createuser(__id, __hashed_password, __token)

    def retrieve_user_bytoken(self, token: str) -> User:
        query: str = "SELECT id, password, token, expires_in FROM users WHERE token=%s"
        self.cursor.execute(query, (token, ))
        res = self.cursor.fetchone()
        __id: Id = Id(res[0])
        __hashed_password: HashedPassword = HashedPassword(res[1])
        __token: Token = Token(res[2], res[3])
        return self.userfactory.createuser(__id, __hashed_password, __token)

    def add(self, user: User):
        query: str = "INSERT INTO users (id, password, token, expires_in) VALUES (%s, %s, %s, %s)"
        __id: str = user.get_id().get_id()
        __hashed_password: str = user.get_password().get_password()
        __token: str = user.get_token().get_token()
        __expires_in: int = user.get_token().get_expires_in()
        self.cursor.execute(query, (__id, __hashed_password, __token, __expires_in))
        self.connection.commit()

    def store(self, user: User):
        query: str = "UPDATE users SET password=%s, token=%s, expires_in=%s WHERE id=%s"
        __id: str = user.get_id()
        __hashed_password: str = user.get_password()
        __token: str = user.get_token().get_token()
        __expires_in: int = user.get_token().get_expires_in()
        self.cursor.execute(query, (__hashed_password, __token, __expires_in, __id))
        self.connection.commit()

    def delete(self, id: Id):
        query: str = "DELETE FROM users WHERE id=%s"
        self.cursor.execute(query, (id.get_id(), ))
        self.connection.commit()