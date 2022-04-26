
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



def create_new_credential(user_name,website_name,account_name,password):
        '''
        A function that creates a new credential for a given user account.
        '''
        new_credential=Credential(user_name,website_name,account_name,password)
        return new_credential
def save_credentials(credentials):
        '''
        A function that saves a newly created credential for the user
        '''
        Credential.save_credentials(credentials)
def display_usercredentials(user_name):
        '''
        Function to display credentials saved by a user
        '''
        return Credential.display_credentials(user_name)


