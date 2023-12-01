
import maskpass
import time
from model.store_model import StoreModel
from view.store_view import StoreView
from controller.validate_controller import ValidateController

class StoreController:
    def __init__(self):
        self.model = StoreModel()
        self.view = StoreView()
        self.validate = ValidateController()
        
#Function to display the CART:

    def view_cart(self,viewcart):
        self.view.display_cart(viewcart)

#Function to display Orders placed by the user:

    def your_orders(self,email):
        data = self.model.get_orders(email)
        self.view.display_orders(data)

#Function where user interacts, view products, place order :

    def home(self,email):
        viewcart={}
        while 1:
            c=input("\n1.Buy products\n2.View Cart\n3.Your Orders\n4.Log Out\n")          
            if c=="1":
                cloth={"\nT-shirt":500,"Jeans":700,"Shirts":400,"Pants":300,"Shorts":250,"Jerkins":1000,"Saree":1200,"Chudi":800}
                for key, value in cloth.items():
                    print(key+":",value)
                get=input("\nWhat do you want : ")
                if get in cloth:
                    ch=input("\n1.Buy Now\n2.Add to Cart\n3.Back to main menu\n")
                    if ch=="1":
                        while True:
                            quantity=int(input("Enter Quantity : "))
                            try:
                                if quantity>0 and quantity<=10:
                                    break
                                else:
                                    raise ValueError                                  
                            except ValueError:
                                print("Maximum Quantity is 10!!!\n")
                        while True:
                            size=input("Which size do you want : ")
                            try:                                    
                                if size == "S" or size == "M" or size == "L" or size == "XL" or size =="XXL":
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print ("\nEnter Valid Size..!!\n")
                        print("Proceeding to Checkout...\n")
                        price=cloth[get]
                        h.checkout(email,get,quantity,price)
                    elif ch=="2":
                        viewcart.update({get:cloth[get]}) 
                        print("\nProduct added to cart :) ")
                        
                    elif ch=="3":
                        break
                    else:
                        print("Enter valid input\n")
                else:          
                    print("\nProduct Not available\n")

            elif c=="2":
                h.view_cart(viewcart)

            elif c=="3":
                h.your_orders(email)

            elif c=="4":
                print(">>>>>>Sucessfully Logged out<<<<<<\n")
                time.sleep(2)
                break

            else:
                print("\nEnter Valid input..\n")

#Function to proceed to CHECKOUT :
    
    def checkout(self,email,product,quantity,price):
        while True:
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
                            self.view.order_placed()
                            self.model.checkout(email,product,quantity,price)
                            break
                        elif f=="2":
                            break                      
                    if ch=="2":
                        break
                    else:
                        print("Enter valid input\n")
                elif pay=="2":
                    add=input("Enter your address : ")
                    while True:
                        f=input("\n1.Place order\n2.Cancel Order\n")
                        if f=="1":
                            self.view.order_placed()
                            self.model.checkout(email,product,quantity,price)
                            break
                        elif f==2:
                            break
                        else:
                            print("Invalid Input..")     
                elif pay=="3":
                    break 
                else:
                    print("Enter valid input.")
            elif z=="2":
                break
            else:
                print("Enter valid input\n")
            break

#Function to get Card details : 

    def getcard(self):
        print("Please add your card details..")
        card= self.validate.validate_card()   
        expiry=input("Expiry date : ")
        name=input("Card holder's name : ")
        while True:
            cvv = maskpass.askpass(prompt="CVV : ", mask="*")
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

h = StoreController()