import unittest
from typing import Protocol

from application.userrepository import UserRepository
from domain.id import Id
from domain.hashedpassword import HashedPassword
from domain.token import Token
from domain.user import User
from application.userrepository import UserRepository
from infrastructure.userrepositoryimpl import UserRepositoryMySQL
from factory.userfactoryimpl import UserFactoryImpl
from factory.userfactory import UserFactory

class TestUserRepositoryMySQL(unittest.TestCase):
    userfactory: UserFactory = UserFactoryImpl()
    repository: UserRepository = UserRepositoryMySQL(userfactory)

    def test_id_exists(self):
        print("\033[05;44m" + "test_id_exists" + "\033[0m")
        userid: Id = Id("horizon")
        id_exists: bool = self.repository.id_exists(userid)
        self.assertTrue(id_exists)

    def test_id_not_exists(self):
        print("\033[05;44m" + "test_id_not_exists" + "\033[0m")
        userid: Id = Id("nothorizon")
        id_exists: bool = self.repository.id_exists(userid)
        self.assertFalse(id_exists)
        
if __name__ == "__main__":
    unittest.main()
