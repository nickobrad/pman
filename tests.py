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

    def test_user_exists(self):
        self.user.save_user() 
        fake_user = User ("aaa", "bbb", "ccc", "111")
        fake_user.save_user()
        user_lives = User.user_verification("ccc")
        self.assertTrue(user_lives)

    def test_account_exists(self):
        self.acc.save_account()
        fake_acc = Credentials("qqq", "rrr", "222")
        fake_acc.save_account()
        acc_lives = Credentials.account_verification("qqq")
        self.assertTrue(acc_lives)

    def test_account_delete(self):
        self.acc.save_account()
        fake_acc = Credentials("qqq", "rrr", "222")
        fake_acc.save_account()
        self.acc.delete_account()
        self.assertEqual(len(Credentials.accountList),1)


if __name__ == '__main__':
    unittest.main()