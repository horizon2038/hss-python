from ast import Pass
import hashlib

from domain.password import Password
from domain.hashedpassword import HashedPassword

from domain.passwordhashgenerator import PasswordHashGenerator #Interface

from domain.password import Password

class PasswordHashGeneratorImpl():
    def __init__(self):
        pass

    def __generate_md5(self, password: str) -> str:
        md5_hashed_password: str = hashlib.md5(password.encode()).hexdigest()
        return md5_hashed_password

    def __generate_sha256(self, password: str) -> str:
        sha256_hashed_password: str = hashlib.sha256(password.encode()).hexdigest()
        return sha256_hashed_password

    def __extract_8word(self, password: str) -> str:
        return password[0:7]

    def __generate_salt(self, password: str) -> str:
        md5_hashed_salt: str = self.__generate_md5(password)
        salt: str = self.__extract_8word(md5_hashed_salt)
        return salt

    def generate_hash(self, password: Password) -> HashedPassword:
        salt: str = self.__generate_salt(password.get_password())
        salt_added_password = password.get_password() + salt
        hashed_password: str = self.__generate_sha256(salt_added_password)
        return HashedPassword(hashed_password)

if __name__ == "__main__":
    passwordhashgenerator: PasswordHashGenerator = PasswordHashGeneratorImpl()
    password: Password = Password("testpassword")
    hashedpassword: HashedPassword = passwordhashgenerator.generate_hash(password)
    print(hashedpassword.get_password())