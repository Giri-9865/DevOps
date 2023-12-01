"""
                            Title              : Online Cloth Store
                            Author             : Girivel R
                            Created on         : 31 Jan 2023
                            Last Modified Date : 15 July 2023
                            Reviewed by        : 
                            Reviewed on        : 

"""
from controller.store_controller import StoreController
from controller.login_controller import LoginController

c = LoginController()

print("\n\n>>>>>>WELCOME TO THE STORE<<<<<<<\n")
while True:
    print("\n1.Existing User\n2.New User")
    choice = input()
    if choice == "1":
        c.login()
    elif choice == "2":
        c.signup()
    else:
        print("\nInvalid input\n")
