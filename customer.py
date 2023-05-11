from tkinter import Tk,Entry,Button,Label,Frame,Scrollbar,ttk
from functools import partial
from mysql.connector import Error
import time



class Customer:
    
    def __init__(self,cursor):
        self.customer_cursor = cursor

    def send_to_database_register_customer(self,name,Lastname,address,phone_number,email):

        #get_information
        self.name = name.get()
        self.lastname = Lastname.get()
        self.address = address.get()
        self.phone_number = phone_number.get()
        self.email = email.get()

        if len(self.phone_number)==11:
            #send to database
            sql = "CALL Register_customer1(%s,%s,%s,%s,%s);"
            val = (self.name,self.lastname,self.address,self.phone_number,self.email)
            #excute
            self.customer_cursor.execute(sql,val)
            #commit
            self.customer_cursor.execute('commit')
            recive = self.customer_cursor.fetchall()

            if (recive!=None) and (len(recive)==0):
                recive = 'Register is successful'
                a = Label(self.add_cust,text=recive,bg='#FBFbFC')
                a.place(x =100, y = 360)
                self.delay()
                a.destroy()

            if (recive==None):
                recive = 'Register is not successful'
                a = Label(self.add_cust,text=recive,background='#FBFbFC')
                a.place(x =100, y = 360)
                self.delay()
                a.destroy()

            #reset entery
            name.delete(0,'end')
            Lastname.delete(0,'end')
            address.delete(0,'end')
            phone_number.delete(0,'end')
            email.delete(0,'end')
        else :
            a = Label(self.add_cust,text='please complete field Phone Number! ',bg='#FBFbFC')
            a.place(x =90, y = 360)
            self.delay()
            a.destroy()
    
    def get_data(self):
        return self.primary_add_data()

    def delay(self):
        for i in range(10000):
            t=0

    def send_to_database_search_customer(self,name,Lastname,phone_number):

        #get_information
        self.name = name.get()
        self.lastname = Lastname.get()
        self.phone_number = phone_number.get()

        #send to database
        try :
            if self.phone_number != None :
                sql ="CALL search_customer_by_phone_number(%s);"
                val = ((self.phone_number,))
                self.customer_cursor.execute(sql,val)
                data = self.customer_cursor.fetchall()
                self.customer_cursor.execute('commit')
                
                if data != None:

                    #delete if exist data
                    for i in range(len(data)):
                        self.my_table.delete(parent='',index='end',iid=i)

                    # add search data to table
                    for i in range(len(data)):
                        self.my_table.insert(parent='',index='end',iid=i,text='',
                        values=self.data[i])

            # if self.phone_number != None :
            #     database.set_query("CALL Register_costumer(%s,%s,%s,%s,%s);")
            #     database.set_val((self.name,self.lastname,self.address,self.phone_number,self.email))

            
            #reset entery
            name.delete(0,'end')
            Lastname.delete(0,'end')
            phone_number.delete(0,'end')

        except Error as e:
             print("Error while connecting to MySQL", e)

    def customer_table(self,data):
        self.top = Tk()
        self.top.title('Customers')
        self.top.geometry('1000x800')
        self.top.resizable(0,0) 
        self.top.config(bg='#FBFbFC')
        #fram table
        main_frame = Frame(self.top,bg='blue')
        main_frame.place(x=0,y=50)

        #scrollbar
        scroll = Scrollbar(main_frame)
        scroll.pack(side='right', fill='y')
        #table
        self.my_table = ttk.Treeview(main_frame,yscrollcommand=scroll.set)
        self.my_table.config(height=35)
        scroll.config(command=self.my_table.yview)

        #define our column
        self.my_table['columns'] = ('c_id','customer_name', 'customer_lastname','address', 'phone_number' 
                                    , 'email')
        # format our column
        self.my_table.column("#0", width=0,  stretch='no')
        self.my_table.column("c_id",anchor='center', width=100)
        self.my_table.column("customer_name",anchor='center', width=100)
        self.my_table.column("customer_lastname",anchor='center',width=200)
        self.my_table.column("address",anchor='center',width=200)
        self.my_table.column("phone_number",anchor='center',width=200)
        self.my_table.column("email",anchor='center',width=200)
        
        # Create Headings 
        self.my_table.heading("#0",text="",anchor='center')
        self.my_table.heading("c_id",text="C_id",anchor='center')
        self.my_table.heading("customer_name",text="Name",anchor='center')
        self.my_table.heading("customer_lastname",text="LastName",anchor='center')
        self.my_table.heading("address",text="Address",anchor='center')
        self.my_table.heading("phone_number",text="Phone_Number",anchor='center')
        self.my_table.heading("email",text="Email",anchor='center')
           
        # add data 
        self.data = data
        for i in range(len(self.data)):
            self.my_table.insert(parent='',index='end',iid=i,text='',
            values=self.data[i])
        
        self.search()
        self.my_table.pack()
        self.my_table.mainloop() 
    
    def primary_add_data(self):
        sql ="CALL get_customer;"
        val = (None)
        self.customer_cursor.execute(sql,val)
        data = self.customer_cursor.fetchall()
        return data

    def search(self):
        #name
        Label(self.top, text ="First Name",bg='#FBFAFC').place(x=10,y=6)
        name = Entry(self.top)        
        name.place(x=90,y=6)

        #lastname
        Label(self.top, text ="LastName",bg='#FBFAFC').place(x=322,y=10)
        Lastname = Entry(self.top)        
        Lastname.place(x=394,y=10)

        #phone_number
        Label(self.top, text = "Phone Number",bg='#FBFAFC').place(x =595, y = 10)
        phone_number = Entry(self.top)
        phone_number.place(x=700,y=10)

        self.send_to_database_search_customer = partial(self.send_to_database_search_customer,name,Lastname,phone_number)
        save = Button(self.top,command=self.send_to_database_search_customer, text = "Search").place(x =900, y =6)
    
    def add_customer(self):
        
        self.add_cust = Tk()
        self.add_cust.title('Customer')
        self.add_cust.geometry('670x400')
        self.add_cust.config(bg='#FBFAFC')
        self.add_cust.resizable(0,0)
        
        #title window
        Label(self.add_cust, text='Welcom to page Register Costumer',bg='#FBFAFC').pack(pady=10)

        #name
        Label(self.add_cust, text ="First Name",bg='#FBFAFC').place(x=100,y=70)
        name = Entry(self.add_cust)        
        name.place(x=100,y=100)
        
        #lastname
        Label(self.add_cust, text ="LastName",bg='#FBFAFC').place(x=400,y=70)
        Lastname = Entry(self.add_cust)        
        Lastname.place(x=400,y=100,width=157)

        #address
        Label(self.add_cust, text = "Address",bg='#FBFAFC').place(x = 100, y = 140)
        address = Entry(self.add_cust,width=57)
        address.place(x=100,y=170)

        #phone_number
        Label(self.add_cust, text = "Phone Number",bg='#FBFAFC').place(x = 100, y = 230)
        phone_number = Entry(self.add_cust,fg='blue')
        phone_number.place(x=100,y=250)

        #email
        Label(self.add_cust, text = "Email",bg='#FBFAFC').place(x = 400, y = 230)
        email = Entry(self.add_cust)
        email.place(x=400,y=250,width=157)
        
        
        self.send_to_database_register_customer= partial(self.send_to_database_register_customer,name,Lastname,address,phone_number,email)
        save = Button(self.add_cust, text = "Register",command=self.send_to_database_register_customer).place(x =285, y = 320)

        #loop
        self.add_cust.mainloop()

