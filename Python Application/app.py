"""
                            Title              : Online Cloth Store
                            Author             : Girivel R
                            Created on         : 31 Jan 2023
                            Last Modified Date : 17 Feb 2023
                            Reviewed by        : 
                            Reviewed on        : 

"""
import csv
import mysql.connector
from login import Login
c=Login()
print("\n\n>>>>>>WELCOME TO THE STORE<<<<<<<\n")
while True:
    print("1.Existing User\n2.New User")
    choice=(input())
    if choice=="1":
        c.login()
    elif choice=="2":
        c.signup()
    else:
        print("\nInvalid input\n")