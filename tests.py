import unittest
from user_class import User
from credentials_class import Credentials

class TestPMAN(unittest.TestCase):

    def tearDown(self):
        User.userCredentials = []
        Credentials.accountList = []

    def setUp(self):
        self.user = User ("Joe", "Boe", "JB", "12345")
        self.acc = Credentials("guess", "guessyguess", "444")

    def test_save_user(self):
        self.user.save_user() 
        self.assertEqual(len(User.userCredentials),1)


    def test_save_account(self):
        self.acc.save_account()
        self.assertEqual(len(Credentials.accountList),1)

if __name__ == '__main__':
    unittest.main()