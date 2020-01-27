#!/usr/bin/env python3.6
from password import Credentials

def create_password(fname,lname,phone,email):
    '''
    Function to create a new password
    '''
    new_password = Password(fname,lname,phone,email)
    return new_password

    def save_password(password):
    '''
    Function to save password
    '''
    password.save_password()

    def del_password(password):
    '''
    Function to delete a password
    '''
    password.delete_password()

    def find_password():
    '''
    Function that finds a password by number and returns the contact
    '''
    return Password.find_by_password

def check_existing_password():
    '''
    Function that check if a password exists with that number and return a Boolean
    '''
    return Password.password_exist()

def display_password():
    '''
    Function that returns all the saved password
    '''
    return Password.display_password()

def main():

            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cd - create a new password, sp - show password , fp -find a password, ex -exit the password list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New password")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Password ...")
                            p_ = input()

                            print("Email address ...")
                            e_address = input()


                            save_password(create_password(f_name,l_name,p_number,email_address))
                            print ('\n')
                            print(f"New Password {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_password():
                                    print("Here is a list of all your password")
                                    print('\n')

                                    for password in display_password():
                                            print(f"{password.first_name} {password.last_name} .....{password.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_password = input()
                            if check_existing_password(search_password):
                                    search_password = find_password(search_password)
                                    print(f"{search_password.first_name} {search_password.last_name}")
                                    print('-' * 20)

                                    print(f"Password.......{search_password.password}")
                                    print(f"Email address.......{search_password.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("Please use the short codes")