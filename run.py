from user import User
import string
import random
import getpass
import pyperclip
from password import Credential
def create_credential(socila_media, passkey):
    '''
    function to create a new credential
    '''
    new_credential = Credential(social_media, passkey)
    return new_credential
def save_credential(credential):
    '''
    function to save a credential
    '''
    credential.save_credential()
def display_credentials():
    '''
    function that dispalys all credentials
    '''
    return Credential.display_credentials()
def delete_credential(credential):
    '''
    function to delete a credential
    '''
    credential.delete_credential()
def check_existing_user(password2):
    '''
    function to check that enable login authentification
    '''
    return User.user_exist(password2)
def find_account(password2):
    '''
    function to find account by its name
    '''
    return User.find_account(password2)
def create_user(f_name, l_name, password,email):
    '''
    function to create a new user
    '''
    new_user = User(f_name, l_name, password,email)
    return new_user
def save_users(user):
    '''
    function to save a user
    '''
    user.save_user()
def display_users():
    '''
    function that dispalys all signed up users
    '''
    return User.display_users()
def main():
    print(f"Hello Welcome to password generator.")
    print("Please sign in to generate your password.")
    print('\n')

    while True:
        print("Select what you want to do  : si - Sign up, lg - login, du-display all users, Ex-Exit passwordgenerator ")
        print('-'*64)
        print('\n')
        short_code = input().lower()
        print('\n')
        if short_code == 'si':
            print("New User")
            print("-"*9)
            print("Enter you first name...")
            f_name = input()
            print("Enter your last name...")
            l_name = input()
            print("Enter your password...")
            password = input()
            print("Enter your email")
            email = input()
            print('\n')
            save_users(create_user(f_name, l_name, password,email))
            print('\n')
            print(
                f"Congratulations {f_name} {l_name} you have created an account\n")
            print('\n')
        elif short_code == 'lg':
                print("Enter the last name of your account")
                account_name = input()
                print('\n')
                authentification = getpass.getpass('Password:')
                if check_existing_user(authentification):
                        search_account = find_account(authentification)
                        print(f"Welcome {search_account.first_name} {search_account.last_name} \n")
                        print("fc-To create new credential, sp-To show passwords, ex-To exit your account \n ")
                        print('-'*80)
                        short_code = input().lower()
                        if short_code == 'fc':
                                print("New credential")
                                print('-'*14)
                                print("Enter your account name")
                                account_name = input()
                                print("Make your password \n")
                                print(
                                "To create your own password press f, to generate a password press ge \n")
                                print('-'*50)
                                generate = input()
                                print('\n')
                                if generate == 'ge':
                                        letters = string.ascii_letters + string.digits
                                        gpassword = ''.join(random.choice(letters)
                                                                for i in range(9))
                                        print(
                                                f"Your new generated password is: {gpassword} \n")
                                        passkey = gpassword
                                elif generate == 'f':
                                        print("Enter your password")
                                        passkey = input()
                                        print('\n')
                                        print(f"{account_name} is saved")
                                        save_credential(create_credential(
                                        account_name, passkey))
                        elif short_code == 'sp':
                                if display_credentials:
                                        print("Here is a list of all your accounts and passwords \n")
                                        for credential in display_credentials():
                                                print(f"Account name: {credential.account_name} - password: {credential.passkey}")
                        elif short_code == 'de':
                                print("Which credential would you like to delete?")
                                del_account = input()
                                if del_account == account_name:
                                        Credential.credential_list.remove(credential)
                                        print("Credential deleted")
                                else:
                                        print("No match of such a credential")
                        elif short_code == 'ex':
                                print("you exited your account\n")
                                break
                else:
                        print("The password was incorrect \n")
                        print('\n')
        elif short_code == 'du':
            print("this is the list of all the users\n")
            for user in display_users():
                print(f"{user.first_name} {user.last_name} \n")
        elif short_code == 'ex':
            print("thank you see you soon\n")
            break
        else:
            print("please use these codes \n")
if __name__ == '__main__':
    main()
