import csv
import re

class Validate:
    @classmethod
    def username(self):
        while 1:
            name=input("Enter user name...")
            pattern=r"^[A-Za-z0-9]{4,29}$"
            if re.findall(pattern,name):
                return name
            else:
                print("Invalid Username !!!")
                print("Please enter valid Username..")
                
    def password(self):
        while 1:
            password=input("Enter a strong Password..")
            if len(password)>8:
                if re.search("[a-z]",password):
                    if re.search("[A-Z]",password):
                        if re.search("[0-9]",password):
                            if re.search("[!@#$%^&*()-/+]",password):
                                return password
            print("Password is TOO WEAK.!!")
            print("Password must contain at least 1 upper case, numeric, and special character")

    def emailid(self):
        while 1:
            flag=True
            email=input("Enter your E-mail ID..")
            with open("users.csv","r+") as file:
                read=csv.reader(file)
                for row in read:
                    if row[1]==email:
                        print("Email ID already registered witth existing account..")
                        flag = False
                        break
                if flag ==True:
                    if email!="NULL":
                        if re.search("[a-z0-9]+@+",email):
                            return email
                    print("Invalid email ID")   

    def mobile(self):
        while 1:
            mobile=input("Enter Your Mobile Number..")
            if re.search("^[6-9]+.........$",mobile):
                return mobile
            else:
                print("Enter a Valid mobile number..")

    def card(self):
        while 1:
            card1=input("Card number : ")
            pattern="\d{16}"
            if re.findall(pattern,card1):
                return card1
            else:
                print("Enter Valid card details..\n")

v=Validate()
 