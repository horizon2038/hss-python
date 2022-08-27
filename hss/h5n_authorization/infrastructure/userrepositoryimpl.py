import hashlib
from application.userrepository import UserRepository
import MySQLdb

class UserRepositoryMySQL(): 
    def __connectDB(self):
        self.connection = MySQLdb.Connect(user='root', passwd='Halcyon441', host='localhost', db='h5nserver')

    def __createcursor(self):
        self.cursor = self.connection.cursor()

    def __init__(self):
        self.__connectDB()
        self.__createcursor()

    def userexists(self, id: str) -> bool:
        query: str = "SELECT EXISTS(SELECT id FROM users WHERE id=%s)"
        self.cursor.execute(query, (id, ))
        res = self.cursor.fetchall()
        return res[0][0]

    def searchpassword_byuserid(self, id: str) -> str:
        query: str = "SELECT id, password FROM users WHERE id=%s"
        self.cursor.execute(query, (id, ))
        res = self.cursor.fetchall()
        return res[0][1]

    def changeuserpassword(self, id: str, password: str):
        query: str = "UPDATE users SET password=%s WHERE id=%s"
        self.cursor.execute(query, (password, id))
        self.connection.commit()

    def adduser(self, id: str, hashed_password: str):
        query: str = "INSERT INTO users (id, password, hash) VALUES (%s, %s, null)"
        self.cursor.execute(query, (id, hashed_password))
        self.connection.commit()

    def deleteuser(self, id: str):
        query: str = "DELETE FROM users WHERE id=%s"
        self.cursor.execute(query, (id, ))
        self.connection.commit()