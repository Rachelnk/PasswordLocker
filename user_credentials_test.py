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



