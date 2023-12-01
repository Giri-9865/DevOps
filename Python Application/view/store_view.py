
class StoreView:
    @staticmethod
    def display_cart(viewcart):
        print("\n>>>>>>>>>The Items In the Cart<<<<<<<<<\n")
        if not viewcart:
            print("\nYour Cart is empty\n")
        else:
            for key, value in viewcart.items():
                print(key, value)
            tot = sum(viewcart.values())
            print("\nTotal amount of products in the cart:", tot)
        print("\n>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")

    @staticmethod
    def display_orders(data):
        print("\n>>>>>>>>>>>>>>YOUR ORDERS<<<<<<<<<<<<<<<\n")
        if not data:
            print("\n No Orders have been placed\n")
        else:
            for row in data:
                user_email,product, quantity, price = row
                print(f"Product: {product}, Quantity: {quantity}, Price: {price}")
        print("\n>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")
    @staticmethod
    def order_placed():
        print("******Order placed succesfully******\n")
        print("\n>>>>>>Continue Shopping<<<<<<\n")