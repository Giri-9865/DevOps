
class LoginView:
    @staticmethod
    def display_login_success():
        print("\n\n>>>>Login Successful<<<<\n")

    @staticmethod
    def display_invalid_credentials():
        print('\n\nInvalid Email ID or password. Please try again..\n\n')
    
    @staticmethod
    def signup_failed():
        print("\n\nPasswords don't match..")