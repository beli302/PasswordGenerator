from password import Credential
class User:
    '''
    class that generates new instances of users accounts
    '''
    user_list = []  
    def save_user(self):
        '''
        save users
        '''
        User.user_list.append(self)
    def __init__(self, first_name, last_name, password,email):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email 

    @classmethod
    def display_users(cls):
        '''
        display all the users
        '''
        return cls.user_list
    @classmethod
    def user_exist(cls, password):
        '''
        checks if a user and
        their details exist
        '''
        for user in cls.user_list:
            if user.password == password:
                return True
        return False
    @classmethod
    def find_account(cls, password2):
        '''
        finds an account by its name
        '''
        for user in cls.user_list:
            if user.password == password2:
                return user