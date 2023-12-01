
import mysql.connector
import time

class StoreModel:
    @classmethod

#Function to retrieve Order details from DataBase :

    def get_orders(cls,email):        
        pydb=mysql.connector.connect(host = "localhost",
                                    user = "root",
                                    passwd = "Girivel@9865",
                                    auth_plugin="mysql_native_password",
                                    database = "store")
        curs = pydb.cursor()
        query = "SELECT * FROM orders where user_email = %s"
        curs.execute(query,(email,))
        data = curs.fetchall()
        pydb.close()
        return data
    @classmethod

#Funtion to store Order detals in the DataBase : 

    def checkout(cls,email,product,quantity,price):
        pydb=mysql.connector.connect(host = "localhost",
                                    user = "root",
                                    passwd = "Girivel@9865",
                                    auth_plugin="mysql_native_password",
                                    database = "store")
        curs=pydb.cursor()
        query = "INSERT INTO orders VALUES (%s,%s,%s,%s)"
        value = (email,product,quantity,price)
        curs.execute(query,value)
        pydb.commit()
        pydb.close()
        time.sleep(2)
