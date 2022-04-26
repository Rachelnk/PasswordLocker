
#! /usr/bin/env python3
import pyperclip
from user_credentials import User, Credential

def create_user(fname,lname,password):
        '''
        A function that create a new user account
        '''
        new_user = User(fname,lname,password)
        return new_user

def save_newuser(user):
        '''
        A function that save a new user account
        '''
        User.save_newuser(user)

def verify_user(first_name,password):
        '''
        A function that checks if the users exists
        '''
        checking_user = Credential.check_user(first_name,password)
        return checking_user

def generate_password():
        '''
        A function that generate a password automatically
        '''
        generate_userpassword = Credential.generate_password()
        return generate_userpassword



def create_new_credential(user_name,website_name,password):
        '''
        A function that creates a new credential for a given user account.
        '''
        new_credential=Credential(user_name,website_name,password)
        return new_credential
def save_credentials(credentials):
        '''
        A function that saves a newly created credential for the user
        '''
        Credential.save_credentials(credentials)
def display_usercredentials(user_name):
        '''
        A function that displays credentials saved by a user.
        '''
        return Credential.display_credentials(user_name)
def delete_credential(credentials):
        """
        A function that deletes a credential from the credentials list.
        """
        credentials.delete_credentials()
def copy_credential(site_name):
        '''
        A function that copies credentials details to the clipboard
        '''
        return Credential.copy_credential(site_name)
def main():
        print('')
        print('Hello there! Welcome to your Account\'s password store. ')
        while True:
                print('')
                print("-"*60)
                print('Use these short codes to navigate through application: \n ca-Create an Account \n li-Log In \n ex-Exit')
                short_code = input('Enter a short code: ').lower().strip()
                if short_code == 'ex':
                        break
                #break the while loop because the user has choosen to exit.
                elif short_code == 'ca':
                        print('')
                        print("-"*60)			
                        print('To create a new create, do the following:')
                        first_name = input('Enter your first name - ').strip()
                        last_name = input ('Enter your last name -').strip()
                        password = input ('Enter your password -').strip()
                        #strip() to remove whitespaces at the beginning and the end of the string.
                        save_newuser(create_user(first_name,last_name,password))
                        print("")
                        print(f'New account created for: {first_name} {last_name} using password: {password}')
                elif short_code == 'li':
                        #login
                        print("-"*60)
                        print('')
                        print('To login, enter your account details:')
                        username = input('Enter you first name: ').strip()
                        password = str(input('Enter your password: '))
                        user_exists = verify_user(username, password)
                        if verify_user == user_exists:
                                print("")
                                print(f'Login successful. Welcome {username}. Please choose an option to continue.')
                                print('')
                                while True:
                                        print("-"*60)
                                        print('Enter a short code: \n cc-Create a credential \n dc-Display credentials \n copy-Copy password \n del-Delte \n ex-Exit')
                                        short_code = input('Enter : ').lower().strip()
                                        print("-"*60)
                                        if short_code == 'ex':
                                                #user wants to exit
                                                print("")
                                                print(f'Goodbye {username}')
                                                break
                                        elif short_code == 'cc':
                                                #user wants to create a credenetial
                                                print ('')
                                                print('Enter your credential details:')
                                                site_name = input('Enter the site\'s name-').strip()
                                                
                                                while True:
                                                        print('')
                                                        print("-"*60)
                                                        print('Please choose an option for creating a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                                                        psw_choice = input('Enter an option: ').lower().strip()
                                                        print("-"*60)
                                                        if psw_choice == 'ep':
                                                                #user entered the existing password option
                                                                print("")
                                                                password = input("Enter your password: ").strip()
                                                                break
                                                        elif psw_choice == 'gp':
                                                                #generate password was entered
                                                                password = generate_password()
                                                                break
                                                        elif psw_choice == 'ex':
                                                                break
                                                        else:
                                                                print('Wrong option entered. Please try again.')
                                                save_credentials(create_new_credential(username,site_name,password))
                                                print('')
                                                print(f'Credentials created: Site name {site_name} - password {password}')
                                                print('')
                                        elif short_code == 'dc':
                                                print('')
                                                if display_usercredentials(username):
                                                        print('Here is a list of all your credentials')
                                                        print('')
                                                        for credential in display_usercredentials(username):
                                                                print(f'Site Name: {credential.website_name} - Password: {credential.password}')
                                                        print('')
                                                else:
                                                        print('')
                                                        print("You don't seem to have any credentials saved yet")
                                                        print('')
                                        elif short_code == 'copy':
                                                print('')
                                                site_chosen = input('Enter the site name for the credential password to copy: ')
                                                copy_credential(site_chosen)
                                                print('')
                                        else:
                                                print('You entered the wrong option. Try again.')
                else:
                        print('')
                        print('Oops! Wrong details entered. Try adain or create an account.')
        else:
                print("-"*60)
                print('')
                print('Oops. Wrong option entered. Try again.')


if __name__ == '__main__':
        main()
                




                        







                                












                                                        
                       

                        





                        
                        






