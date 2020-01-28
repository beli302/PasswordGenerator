class Credentials:
    """
    Class that generates new instances of Password
    """    

    credentials_list = [] 
    password_list = []

    def __init__(self,first_name,last_name,password,email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email 

 
 
    def save_credentials(self):
        '''
        save_credentials method saves password objects into password_list
        '''

        Credentials.password_list.append(self)
        
    def delete_password(self):

        '''
        delete_password method deletes a saved password from the password_list
        '''

        Credentials.password_list.remove(self)

    @classmethod
    def display_passwords(cls):
        '''
        method that returns the password list
        '''
        return cls.password_list

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found password
        '''

        self.new_password.save_password()
        Password.copy_email("")

        self.assertEqual(self.new_password.email,pyperclip.paste())

    @classmethod
    def copy_email(cls,number):
        password_found = Password.find_by_password
        pyperclip.copy(password_found.email)