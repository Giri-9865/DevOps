import csv
import maskpass
import mysql.connector
from validate import Validate
from home import Home
class Login:
    @classmethod
    # Function to prompt the user to login
    def login(self):
        email1 = input('Enter your registered Email ID: ')
        password1 = maskpass.askpass(prompt="Password:", mask="*")
        email=(email1,)
        password=(password1,)
        flag = True   
        pydb=mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     passwd = "Girivel@9865",
                                     database = "store")
        curs=pydb.cursor()
        query = "select user_email from users"
        curs.execute(query)
        log_in=curs.fetchall()
        query1 ="select user_pass from users where user_email= %s"
        curs.execute(query1,email)
        log_pass=curs.fetchone()
        for row in log_in:
            if row ==email:
                if log_pass == password:
                    print("\n\n>>>>Login Successful<<<<\n")
                    h.home()
                    flag = False
                    break
        if flag==True:  
            print('\n\nInvalid Email ID or password. Please try again..\n\n')
                      
    def signup(self):
        while True:
            flag=True
            with open("users.csv","a+",newline="") as file:
                writer=csv.writer(file)
                username=v.username()
                email_id=v.emailid()
                mobile=v.mobile()
                password=v.password()
                repass=input("Re Enter the password...")
                if password==repass: 
                    pydb=mysql.connector.connect(host = "localhost",
                                                 user = "root",
                                                 passwd = "Girivel@9865",
                                                 database = "store")
                    curs=pydb.cursor()
                    query="INSERT INTO users (username,user_email,user_pass,mobile) VALUES (%s,%s,%s,%s)"
                    value=(username,email_id,password,mobile)
                    curs.execute(query,value)   
                    pydb.commit()
                    break
                else:
                    print("Passwords doesn't match..")
        print("Please Login ...")
        s.login()
    
s=Login()
v=Validate()
h=Home()