import mysql.connector
from mysql.connector import Error


class Database:

  def __init__(self,query=None,val=None):

    self.query = query
    self.val = val  
    self.mydb = mysql.connector.connect(
        host="localhost",
        user="debian-sys-maint",
        password="gZQjWpPt8hrFaxlF",
        database="Tools_Store"
    )

  def set_query(self,query:str,val:set = None):
    self.query = query
    self.val = val
  
  def get_query(self):
    return [self.query,self.val]

  def exit(self):
    self.cursor.close()
    self.mydb.close()
    print("MySQL connection is closed")
    

  def connect(self):

    # Preparing SQL query to INSERT a record into the database.
    # sql = "CALL get_costumer();"
    # val = ('John', 'nnn','hh','09387145655','email_l')

    try:
      
      if self.mydb.is_connected():

        db_Info = self.mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info,"\n#################################################")
        
        self.cursor = self.mydb.cursor()
        self.cursor.execute(self.get_query()[0],self.get_query()[1])
        # self.cursor.execute()

        recive = self.cursor.fetchall()
  
        if len(recive)== 0:
          return 'operation is successfull:)'

        else: 
          return recive
        

        # self.mydb.commit()

    except Error as e:
        
        print("Error while connecting to MySQL", e)

    
        
database = Database()
# print(database)

