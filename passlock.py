import random
import string
import pyperclip

global users_list 
# users list is variable that is accessible throughout the program

class User:
        '''Class to create user accounts and save user information and generates new instances of user
        '''
        users_list = []
        def __init__(self, first_name, last_name, password):
          '''
          Method to define the properties that each user objects will hold.
          '''
          self.first_name = first_name
          self.last_name = last_name
          self.password = password

        def save_newuser(self):
          
          User.users_list.append(self)



