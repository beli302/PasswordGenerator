from password import Credentials

def create_password(firstname,lastname,password,email):
    '''
    Function to create a new password
    '''
    new_password = Password(fname,lname,password,email)
    return new_password

def save_credentials(credentials):
     '''
    Function to save credentials
     '''
     credentials.save_credentials()

def del_password(password):
     '''
    Function to delete a password
     '''
     password.delete_password()

def find_password():
      '''
    Function that finds a password 
      '''
      return Password.find_by_password

def check_existing_password():
    '''
    Function that check if a password exists
    '''
    return Password.password_exist()

def display_password():
    '''
    Function that returns all the saved password
    '''
    return Credentials.display_passwords()
def create_credentials(f_name,l_name,p_,e_address):
     '''
    Function to save credentials
     '''
     credentials = Credentials(f_name,l_name,p_,e_address)
     return credentials
def main():

            user_name = input()

            print(f"Hello {user_name} Welcome to password generator.")
            print("Please sign in to generate your password.")
            print('\n')

            while True:
                    print("Select what you want to do  : cp - create a new password, sp - show password , fp -find a password, ex -exit the password list ")

                    short_code = input().lower()

                    if short_code == 'cp':
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


                            save_credentials(create_credentials(f_name,l_name,p_,e_address))
                            print ('\n')
                            print("New Password for {f_name} {l_name} created \n")
                            print ('\n')

                    elif short_code == 'sp':

                            if display_password():
                                    print("Here is a list of all your password")
                                    print('\n')

                                    for password in display_password():
                                            print(f"{password.first_name} {password.last_name} .....{password.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter your password")

                            search_password = input()
                            if check_existing_password(search_password):
                                    search_password = find_password(search_password)
                                    print(f"{search_password.first_name} {search_password.last_name}")
                                    print('-' * 20)

                                    print(f"Password.......{search_password.password}")
                                    print(f"Email address.......{search_password.email}")
                            else:
                                    print("That password does not exist")

                    elif short_code == "ex":
                            print("Thank You .......")
                            break
                    else:
                            print("Please use the short codes")

if __name__ == '__main__':

    main()