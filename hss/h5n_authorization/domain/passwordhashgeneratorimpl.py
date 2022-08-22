import hashlib

from domain.passwordhashgenerator import PasswordHashGenerator #Interface

from domain.password import Password

class PasswordHashGeneratorImpl():
    def __init__(self):
        pass

    def __generatesalt(self, password: str):
        md5hashedpassword: str = hashlib.md5(password.encode()).hexdigest()
        return md5hashedpassword
    
    def __extract8word(self, password: str):
        return password[0:7]

    def generatehash(self, password: str):
        salt: str = self.__generatesalt(password)
        salt8word = self.__extract8word(salt)
        saltaddedpassword = password + salt8word
        hashedpassword: str = hashlib.sha256(saltaddedpassword.encode()).hexdigest()
        return hashedpassword