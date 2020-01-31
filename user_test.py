import unittest  # unnitest module import
from user import User
class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_user = User("Belinda", "okumu", "576890")
    def test_init(self):
        '''
        test_init checks if the object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name, "Belinda")
        self.assertEqual(self.new_user.last_name, "Okumu")
        self.assertEqual(self.new_user.password, "576890")
        self.assertEqual(self.new_user.email, "belindashirkiz1@gmail.com") 
    def test_save_user(self):
        '''
        test_save_user tests if a new user created is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 3)
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user tests if many users can be saved
        '''
        self.new_user.save_user()
        test_user = User("test", "user", "beli")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
    def test_display_users(self):
        '''
        method that displays all thes signed up users
        '''
        self.assertEqual(User.display_users(), User.user_list)
    def test_user_exist(self):
        '''
        test to check if a user exists in user list
        '''
        self.new_user.save_user()
        test_user = User("test", "lname", "passw")
        test_user.save_user()
        user_exists = User.user_exist("test")
        self.assertTrue(user_exists)
if __name__ == '__main__':
    unittest.main()