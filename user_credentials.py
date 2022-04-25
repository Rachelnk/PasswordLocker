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
          '''
          Create function to save a newly created user interface       
          '''
          
          User.users_list.append(self)
          
class Credential:
        '''
        Credentials class to create user credentials, generate passowrds and save passwords. 
        '''
        credentials_list= []
        user_credentials_list = []

        @classmethod
        def check_user(cls, first_name, password):
                '''
                Function to check if the name and password provided matches those in the users_list.
                '''
                existing_user = ''
                # declare  variable of type string
                for user in User.users_list:
                        if (user.firstname == first_name and user.password == password):
                          existing_user = user.first_name
                return existing_user

        def __init__(self,username, website_name, account_name, password):
                self.username = username
                self.website_name = website_name
                self.account_name = account_name
                self.password = password

        def save_credentials(self):
              '''
              Method to save user's credentials
              '''
              Credential.credentials_list.append(self)



          

        
      









