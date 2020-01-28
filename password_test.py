import unittest 
from password import Credentials
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the password class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Credentials("Belinda","Okumu","56789","belindashirkiz2@gmail.com")


    def test__init__(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"Belinda")
        self.assertEqual(self.new_password.last_name,"Okumu")
        self.assertEqual(self.new_password.email,"belindashirkiz2@gmail.com")

    def test_save_password(self):
        '''
        test_save_password test case to test if the password object is saved into
         the user_password_list
        '''
        self.new_password.save_credentials()
        self.assertEqual(len(Credentials.user_password_list),1)


    def test_save_multiple_password(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our user_password_list
            '''
            self.new_password.save_password()
            test_password = Password("Test","","","")
            test_password.save_password()
            self.assertEqual(len(Password.user_password_list),2)

    def tearDown(self):
            '''
            this does the clean up after each test has run.
            '''
            Credentials.user_password_list = []

    def test_save_multiple_password(self):
            '''
             this test saves multiple_passwords in our user_password_list
            '''
            self.new_password.save_credentials()
            test_password = Credentials("Test","","","")
            test_password.save_credentials()
            self.assertEqual(len(Credentials.user_password_list),2)


    def test_delete_password(self):
            '''
            test_delete_password to test if we can remove a password from our user_password_list
            '''
            self.new_password.save_credentials()
            test_password = Credentials("Test","","","")
            test_password.save_credentials()

            self.new_password.delete_password()
            self.assertEqual(len(Credentials.user_password_list),1)


    def test_display_all_passwords(self):
        '''
        this returns a list of all paswords saved
        '''
        self.assertEqual(Credentials.display_passwords(),Credentials.user_password_list)

if __name__ == '__main__':
    unittest.main()