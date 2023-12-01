
import re
import mysql.connector

class ValidateModel:
    @classmethod

#Function to check for Existing Accounts while Signing Up :

    def check_existing_email(cls,email):
        pydb=mysql.connector.connect(host = "localhost",
                                    user = "root",
                                    passwd = "Girivel@9865",
                                    auth_plugin="mysql_native_password",
                                    database = "store")
        curs = pydb.cursor()
        query = "SELECT user_email FROM users WHERE user_email = %s"
        curs.execute(query,(email,))
        existing_email = curs.fetchone()
        pydb.close()
        return existing_email
