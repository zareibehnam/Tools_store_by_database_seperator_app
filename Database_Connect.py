import mysql.connector
from mysql.connector import Error


class Database:

  def __init__(self):
      try:
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="tools_store",
                    database="Tools_Store"
                    )

        if self.mydb.is_connected():
          db_Info = self.mydb.get_server_info()
          print("Connected to MySQL Server version ", db_Info,"\n#################################################")
          self.cursor = self.mydb.cursor()

      except Error as e:
        print("Error while connecting to MySQL", e)
    
  def connect(self):
    return self.cursor

main_database = Database()
# customer_database = Database()
# product_database = Database()
