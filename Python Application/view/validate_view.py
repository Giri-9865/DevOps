
class ValidateView:
    @staticmethod
    def display_invalid_username():
        print("Invalid Username !!!")
        print("Please enter a valid Username.")

    @staticmethod
    def display_weak_password():
        print("Password is TOO WEAK.!!")
        print("Password must contain at least 1 uppercase letter, numeric, and special character.")

    @staticmethod
    def display_existing_email():
        print("Email ID already registered with an existing account.")

    @staticmethod
    def display_invalid_email():
        print("Invalid email ID.")
