import csv
import time
import mysql.connector
from validate import Validate
import re
class Home:
    @classmethod
    def home(self):
        view={}
        while 1:
            c=input("\n1.Buy products\n2.View Cart\n3.Log Out\n")          
            if c=="1":
                cloth={"T-shirt":500,"Jeans":700,"Shirts":400,"Pants":300,"Shorts":250,"Jerkins":1000,"Saree":1200,"Chudi":800}
                for key, value in cloth.items():
                    print(key+":",value)
                get=input("\nWhat do you want : ")
                flag = True
                for x ,y in cloth.items():
                    if get==x:
                        ch=input("\n1.Buy Now\n2.Add to Cart\n3.Back to main menu\n")
                        if ch=="1":
                            while True:
                                q=input("Enter Quantity : ")
                                try:
                                    q=int(q)
                                    if q>0 and q<=10:
                                        break
                                    else:
                                        raise ValueError                                  
                                except ValueError:
                                    print("Maximum Quantity is 10!!!\n")
                            while True:
                                size=str(input("Which size do you want : "))
                                if size=="S" or "M" or "L" or "XL" or "XXl":
                                    break
                                else:
                                    print("Enter the Valid size..\n")
                            print("\n")
                            print("Proceeding to Checkout...\n")
                            pri=y
                            h.checkout(q,pri)
                        elif ch=="2":
                            view.update({x:y}) 
                            print("\nProduct added to cart :) ")
                            flag=False
                        elif ch=="3":
                            break
                        else:
                            print("Enter valid input\n")
                else:            
                    if flag==True:
                        print("\nProduct Not available")

            elif c=="2":
                tot=0
                print("\n>>>>>The Items In the Cart<<<<<\n")
                for key, value in view.items():
                    print(key, value)
                for i in view.values():
                    tot=tot+i
                print("\nTotal amount of products in the cart : ",tot)

            elif c=="3":
                print(">>>>>>Sucessfully Logged out<<<<<<")
                print("\n")
                time.sleep(2)
                break

            else:
                print("\nEnter Valid input..\n")

    def checkout(self,quantity,price):
        while True:
            q=quantity
            p=price
            print("Total Amount : ",quantity*price)
            z=input("\n1.Proceed..\n2.Cancel\n")
            if z=="1":
                pay=input("Select any one of the payment options:\n1.Credit or Debit card\n2.Cash On Delivery\n3.Cancel Payment\n")
                if pay=='1':
                    h.getcard()
                    ch=input("\n1.Proceed to Checkout\n2.Back to main menu\n")
                    if ch=="1":
                        add=input("Enter your address : ")
                        f=input("\n1.Place order\n2.Cancel Order\n")
                        if f=="1":
                            print("*******Order placed succesfully*******\n\n>>>>Continue Shopping<<<<\n")
                            time.sleep(3)
                            break
                        elif f=="2":
                            break                      
                    if ch=="2":
                        break
                    else:
                        print("Enter valid input\n")
                if pay=="2":
                    add=input("Enter your address : ")
                    while True:
                        f=input("\n1.Place order\n2.Cancel Order\n")
                        if f=="1":
                            print("******Order placed succesfully******\n")
                            print("\n>>>>>>Continue Shopping<<<<<<\n")
                            time.sleep(2)
                            break
                        elif f==2:
                            break
                        else:
                            print("Invalid Iput..")     
                if pay=="3":
                    break 
                else:
                    print("Enter valid input.")
            elif z=="2":
                break
            else:
                print("Enter valid input\n")

    def getcard(self):
        print("Please add your card details..")
        card=v.card()                
        expiry=input("Expiry date : ")
        name=input("Card holder's name : ")
        while True:
            cvv=input("CVV : ")
            if len(cvv)==3:
                break
            else:
                print("\nInvalid CVV")
        while True:
            pin=input("Enter your PIN : ")  
            if len(pin)==4:
                break
            else:
                print("Invalid PIN\n")  

h=Home()
v=Validate()