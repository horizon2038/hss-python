import hashlib
import MySQLdb

from application.userrepository import UserRepository
from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User

class UserRepositoryMySQL(): 
    def __connectDB(self):
        self.connection = MySQLdb.Connect(user='root', passwd='Halcyon441', host='localhost', db='h5nserver')

    def __createcursor(self):
        self.cursor = self.connection.cursor()

    def __init__(self):
        self.__connectDB()
        self.__createcursor()

    def exists(self, id: Id) -> bool:
        query: str = "SELECT EXISTS(SELECT id FROM users WHERE id=%s)"
        self.cursor.execute(query, (id.get_id(), ))
        res = self.cursor.fetchall()
        return res[0][0]

    def find_password(self, id: Id) -> HashedPassword:
        query: str = "SELECT password FROM users WHERE id=%s"
        self.cursor.execute(query, (id.get_id(), ))
        res = self.cursor.fetchall()
        return res[0][1]

    def find_token(self, id: Id) -> Token:
        query: str = "SELECT token, expiration_date FROM users WHERE id=%s"
        self.cursor.execute(query, (id.get_id(), ))
        res = self.cursor.fetchall()
        __token: str = res[0][0]
        __expiration_date: int = res[0][1]
        return Token(__token, __expiration_date)

    def add(self, user: User):
        query: str = "INSERT INTO users (id, password, token, expiration_date) VALUES (%s, %s, %s, %s)"
        __id: str = user.get_id()
        __hashed_password: str = user.get_password()
        __token: str = user.get_token().get_token()
        __expiration_date: int = user.get_token().get_expiration_date()
        self.cursor.execute(query, (__id, __hashed_password, __token, __expiration_date))
        self.connection.commit()

    def store(self, user: User):
        query: str = "UPDATE users SET password=%s, token=%s, expiration_date=%s WHERE id=%s"
        __id: str = user.get_id()
        __hashed_password: str = user.get_password()
        __token: str = user.get_token().get_token()
        __expiration_date: int = user.get_token().get_expiration_date()
        self.cursor.execute(query, (__hashed_password, __token, __expiration_date, __id))
        self.connection.commit()

    def delete(self, id: str):
        query: str = "DELETE FROM users WHERE id=%s"
        self.cursor.execute(query, (id, ))
        self.connection.commit()