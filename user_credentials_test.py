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
        Args:
	        unittest.TestCase: helps in creating test cases
        '''
        def test_check_user(self):
                '''
                Function to test whether the login function check_user works as expected
                '''
                self.new_user = User('Rachel', 'Kiarie','pswd1234')
                self.new_user.save_newuser()
                user2 = User('Andrew', 'Kiarie', 'pswd22')
                user2.save_newuser()
                for user in User.users_list:
                        if user.first_name == user2.first_name and user.password == user2.password:
                                current_user = user.first_name
                return current_user
                self.assertEqual(current_user, Credential.check_user(user2.password, user2.first_name))

      
        def setUp(self):
                '''
                Function to create a user's credentials before each test
                '''
                self.new_credential = Credential('Rachel', 'Twitter','raykiarie','pswd123')
        def test__init__(self):
                '''
                Test to if check the initialization/creation of credential instances is properly done
                '''
                self.assertEqual(self.new_credential.user_name,'Rachel')
                self.assertEqual(self.new_credential.site_name,'Twitter')
                self.assertEqual(self.new_credential.account_name,'raykiarie')
                self.assertEqual(self.new_credential.password,'pswd123')
        def test_save_credentials(self):
                '''
                Function to check if the new credential info is saved into the credentials list
                '''
                self.new_credential.save_credentials()
                instagram = Credential("Nduta", "Instagram","ray","pswd123")
                instagram.save_credentials()
                self.assertEqual(len(Credential.credentials_list),2)
        def tearDown(self):
                '''
                Function to clear the credentias_list after every test
                '''
                Credential.credentials_list = []
                User.users_list = []

        def test_display_credentials(self):
                '''
                Test to check if the display_credentials method, displays the correct credentials.
                '''
                self.new_credential.save_credentials()
                twitter = Credential('Nduta','Twitter','rayray','pswd123')
                twitter.save_credentials()
                gmail = Credential('Rachel','Gmail','rachel','pswd123')
                gmail.save_credentials()
                self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)
        def test_copy_credentials(self):
                '''
                Test to check if the copy a credential method copies the correct credential
                '''
                self.new_credential.save_credentials()
                twitter = Credential('Nduta','Twitter','rayray','pswd123')
                twitter.save_credentials()
                find_credential = None
                #assign find_credential variable to a null value
                for credential in Credential.user_credentials_list:
                                find_credential = Credential.find_by_sitename(credential.website_name)
                                return pyperclip.copy(find_credential.password)
                Credential.copy_credential(self.new_credential.site_name)
                self.assertEqual('pswd123', pyperclip.paste())
                print(pyperclip.paste())
if __name__ == '__main__':
        unittest.main()




            




		
		

                














