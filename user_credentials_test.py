import unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
        '''
        A test class that defines test cases for the user class behaviors.

        Args:
            unittest:TestCase TestCase class that helps in creating test cases.
        '''
        def setUp(self):
                '''
                Function to create a user account before each test
                '''
                self.new_user = User('Rachel', 'Kiarie', 'pswd123')
        def test__init__(self):
                '''
                test_init test case to test if the object is initialized properly
                '''
                self.assertEqual(self.new_user.first_name, 'Ray')
                self.assertEqual(self.new_user.last_name,'Kiarie')
                self.assertEqual(self.new_user.password,'pswd123')
        def test_saver_user(self):
                '''
                Test to check if the new users information is saved into the users_list.
                '''
                self.new_user.save_newuser()
                self.assertEqual(len(User.users_list),1)
class TestCredentials(unittest.TestCase):
        '''
        Test class that defines test cases for the credentials class behaviours.
        '''







