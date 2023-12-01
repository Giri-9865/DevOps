import maskpass
from model.login_model import LoginModel
from view.login_view import LoginView
from controller.validate_controller import ValidateController
from controller.store_controller import StoreController

class LoginController:
    def __init__(self):
        self.model = LoginModel()
        self.view = LoginView()
        self.validate_controller = ValidateController()
        self.store_controller = StoreController()
    
#Function which prompts the user to login:

    def login(self):
        email = input('Enter your registered Email ID: ')
        password = maskpass.askpass(prompt="Password:", mask="*")
        user = self.model.authenticate_user(email, password)
        if user:
            self.view.display_login_success()
            self.store_controller.home(email)
        else:
            self.view.display_invalid_credentials()

#Function to signup the new user:

    def signup(self):
        while True:
            username = self.validate_controller.validate_username()
            email_id = self.validate_controller.validate_email()
            mobile = self.validate_controller.validate_mobile()
            password = self.validate_controller.validate_password()
            repass = input("Re Enter the password...")
            if password == repass:
                self.model.signup_user(username, email_id, password, mobile)
                break
            else:
                self.view.signup_failed()

        while True:
            print("\n1.Login Now\n2.Login Later")
            choose = input()
            if choose == "1":
                self.login()
            elif choose == "2":
                break
            else:
                print("\nEnter valid input.!!")
