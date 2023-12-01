
import re
from model.validate_model import ValidateModel
from view.validate_view import ValidateView

class ValidateController:
    def __init__(self):
        self.model = ValidateModel()
        self.view = ValidateView()

    def validate_username(self):
        while 1 :
            name = input ("Enter your username : ")
            if re.search(r"^[A-Z][a-zA-Z0-9]{3,}$", name):
                return name
            else:
                self.view.display_invalid_username()
               
    def validate_password(self):
        while 1 :
            password = input ("Enter a strong Password : ")
            if len(password)>8:
                    if re.search("[a-z]",password):
                        if re.search("[A-Z]",password):
                            if re.search("[0-9]",password):
                                if re.search("[!@#$%^&*()-/+]",password):
                                    return password
            self.view.display_weak_password()

    def validate_email(self):
        while 1 :
            email = input ("Enter your Email ID : ")
            existing_email = self.model.check_existing_email(email)
            if existing_email:
                self.view.display_existing_email()
            elif email != "NULL" and re.search("[a-z0-9]+@+", email):
                
                return email
            else:
                self.view.display_invalid_email()

    def validate_mobile(self):
        while 1 :
            mobile = input ("Enter your Mobile No : ")
            if re.search("^[6-9]+.........$", mobile):
                return mobile
            print("Enter a valid mobile number.")

    def validate_card(self):
        while 1 :
            card =input("Enter your Card Number : ")

            pattern = r"\d{16}"
            if re.search(pattern, card):
                return card
            print("Enter valid card details.")
        
