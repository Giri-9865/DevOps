
import mysql.connector

class LoginModel:
    @classmethod

#Function to authenticate while logging in:

    def authenticate_user(cls, email, password):
        pydb=mysql.connector.connect(host = "localhost",
                                    user = "root",
                                    passwd = "Girivel@9865",
                                    auth_plugin="mysql_native_password",
                                    database = "store")
        curs = pydb.cursor()
        curs.execute("SELECT * FROM users WHERE user_email = %s AND user_pass = %s", (email, password))
        user = curs.fetchone()
        pydb.close()
        return user

#Function to store Credentials of the new users in the DB :

    def signup_user(cls,username, email_id, password, mobile) :
        pydb=mysql.connector.connect(host = "localhost",
                                                user = "root",
                                                passwd = "Girivel@9865",
                                                auth_plugin = "mysql_native_password",
                                                database = "store")
        curs=pydb.cursor()
        query="INSERT INTO users (username,user_email,user_pass,mobile) VALUES (%s,%s,%s,%s)"
        value=(username,email_id,password,mobile)
        curs.execute(query,value)   
        pydb.commit()
        pydb.close()
        return True
