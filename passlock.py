
#! /usr/bin/env python3
import pyperclip
from user_credentials import User, Credential

def create_user(fname,lname,password):
        '''
        A function to create a new user account
        '''
        new_user = User(fname,lname,password)
        return new_user

def save_newuser(user):
        '''
        A function to save a new user account
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
        A function to generate a password automatically
        '''
        generate_userpassword = Credential.generate_password()
        return generate_userpassword


