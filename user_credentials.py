import pyperclip
import random
import string


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

        def delete_user(self):
                '''
                Function that deletes a saved account from the list
                '''
                User.users_list.remove(self)
          
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
                        if (user.first_name == first_name and user.password == password):
                          existing_user = user.first_name
                return existing_user

        def __init__(self,username, website_name, password):
                self.username = username
                self.website_name = website_name
                self.password = password

        def save_credentials(self):
              '''
              Method to save user's credentials
              '''
              Credential.credentials_list.append(self)
        def delete_credentials(self):
              '''
              Method that deletes an account credentials from the credentials_list
              '''
              Credential.credentials_list.remove(self)

        def generate_password(password_size = 8):
                '''
                Method to generate a random password string with 8 characters, digits and special characters.

                '''              
                password_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
                return''.join(random.choice(password_chars ) for i in range(password_size))
        @classmethod
        def display_credentials(cls, user_name):
                '''
                Method that displays the list credentials saved. 
                '''
                user_credentials_list= []
                for credential in cls.credentials_list:
                        if credential.username == user_name:
                                user_credentials_list.append(credential)
                return user_credentials_list
        @classmethod
        def find_credentials(cls, website_name):
                '''
                Method that takes in a site_name and returns a credential that matches that site_name.
                
                '''
                for credential in cls.credentials_list:
                        if credential.website_name == website_name:
                                return credential
        @classmethod
        def copy_credential(cls,site_name):
                '''
                Method that copies a credential's info after the credential's site name is entered
                '''
                find_credential = Credential.find_credentials(site_name)
                return pyperclip.copy(find_credential.password)






        







          

        
      









