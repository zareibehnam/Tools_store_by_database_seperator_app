from tkinter import Tk,Entry,Button,Label,ttk,Menu,StringVar,Menubutton,Frame,Scrollbar
from functools import partial
from mysql.connector import Error


class Product:
    
    def __init__(self,cursor):
        self.product_cursor = cursor     

    def start(self):
        self.root = Tk()
        self.root.title('Product')
        self.root.geometry('670x400')
        self.root.config(bg='#FBFAFC')
        self.root.resizable(0,0)
        self.tools_option = {'digital tools' : ['Mobile phone accessories','Tablet accessories'],
                    'home and kitchen':['Tv','cooler'],'sport':['Men clothing','Women clothing','Bicycle accessories'],
                     'car' : ['Car spare parts','motorcycle spare parts']}
    
    def send_to_database(self,type_tool,brand,name,manufactor,cat_type,price,status,number_of_pro):

        #get_information
        self.type_tool = type_tool.get()
        self.brand = brand.get()
        self.manufactor = manufactor.get()
        self.name = name.get()
        self.cat_type = cat_type.get()
        self.price = int(price.get())
        self.status = status.get()
        self.number_of_pro = int(number_of_pro.get())

        #send to database
        try:
            sql = "CALL Register_category(%s,%s,%s,%s,%s,%s);"
            val = (self.manufactor,self.cat_type,self.name,self.price,self.status,self.number_of_pro)
            self.product_cursor.execute(sql,val)
            id_cat = self.product_cursor.fetchall()
            self.product_cursor.execute('commit')
            
            sql ='select max(Cat_id) from Category;'
            val = (None)
            self.product_cursor.execute(sql,val)
            id_cat = self.product_cursor.fetchall()[0][0]
            self.product_cursor.execute('commit')

            sql ="CALL Register_product(%s,%s,%s);"
            val =(id_cat,self.type_tool,self.brand)
            self.product_cursor.execute(sql,val)
            information = self.product_cursor.fetchall()
            self.product_cursor.execute('commit') 
        except Error as e :
            print('problem to connect: ',e)
        # reset entery
        brand.delete(0,'end')
        type_tool.delete(0,'end')
        manufactor.delete(0,'end')
        name.delete(0,'end')
        cat_type.delete(0,'end')
        price.delete(0,'end')
        status.delete(0,'end')
        number_of_pro.delete(0,'end')

    def send_to_database_search_product(self,name,manufacor,price):

        #get_information
        self.name = name.get()
        self.manufactor = manufacor.get()
        self.price = price.get()
        
        #send to database
        try :
            if self.name != None :
                sql ="CALL search_product_by_name(%s);"
                val = (self.phone_number,)
                self.product_cursor.execute(sql,val)
                self.data = self.product_cursor.fetchall()
                self.product_cursor.execute('commit')

                if self.data != None:
                    #delete if exist
                    for i in range(len(self.data)):
                        self.pro_my_table.delete(parent='',index='end',iid=i)

                    # add search data to table
                    for i in range(len(self.data)):
                        self.pro_my_table.insert(parent='',index='end',iid=i,text='',
                        values=self.data[i])

            # if self.phone_number != None :
            #     database.set_query("CALL Register_costumer(%s,%s,%s,%s,%s);")
            #     database.set_val((self.name,self.lastname,self.address,self.phone_number,self.email))

            
            #reset entery
            name.delete(0,'end')
            manufacor.delete(0,'end')
            price.delete(0,'end')

        except Error as e:
             print("Error while connecting to MySQL", e)

    def product_table(self,data):
        self.pro_table = Tk()
        self.pro_table.title('Products')
        self.pro_table.geometry('1000x800')
        self.pro_table.resizable(0,0) 
        self.pro_table.config(bg='#FBFbFC')
        #fram table
        main_frame = Frame(self.pro_table,bg='blue')
        main_frame.place(x=0,y=50)

        #scrollbar
        scroll = Scrollbar(main_frame)
        scroll.pack(side='right', fill='y')
        #table
        self.pro_my_table = ttk.Treeview(main_frame,yscrollcommand=scroll.set)
        self.pro_my_table.config(height=35)
        scroll.config(command=self.pro_my_table.yview)

        #define our column
        self.pro_my_table['columns'] = ('cat_id','name','manufacor', 'cat_type','status'
                                    ,'price','number_of_pro')
        # format our column
        self.pro_my_table.column("#0", width=0,  stretch='no')
        self.pro_my_table.column("cat_id",anchor='center', width=100)
        self.pro_my_table.column("name",anchor='center', width=100)
        self.pro_my_table.column("manufacor",anchor='center',width=200)
        self.pro_my_table.column("cat_type",anchor='center',width=150)
        self.pro_my_table.column("status",anchor='center',width=150)
        self.pro_my_table.column("price",anchor='center',width=150)
        self.pro_my_table.column("number_of_pro",anchor='center',width=150)
        
        # Create Headings 
        self.pro_my_table.heading("#0",text="",anchor='center')
        self.pro_my_table.heading("cat_id",text="cat_id",anchor='center')
        self.pro_my_table.heading("manufacor",text="manufacor",anchor='center')
        self.pro_my_table.heading("cat_type",text="cat_type",anchor='center')
        self.pro_my_table.heading("name",text="name",anchor='center')
        self.pro_my_table.heading("price",text="price",anchor='center')
        self.pro_my_table.heading("status",text="status",anchor='center')
        self.pro_my_table.heading("number_of_pro",text="number_of_product",anchor='center')

        # add data 
        self.data = data
        for i in range(len(self.data)):
            self.pro_my_table.insert(parent='',index='end',iid=i,text='',
            values=self.data[i])
        
        self.search()
        self.pro_my_table.pack()
        self.pro_my_table.mainloop()

    def primary_add_data(self):
        sql ="CALL get_category;"
        val = (None)
        self.product_cursor.execute(sql,val)
        data = self.product_cursor.fetchall()
        return data

    def search(self):
        #name
        Label(self.pro_table, text ="Name",bg='#FBFAFC').place(x=10,y=6)
        name = Entry(self.pro_table)        
        name.place(x=60,y=6)

        #lastname
        Label(self.pro_table, text ="manufactor",bg='#FBFAFC').place(x=313,y=10)
        manufacor = Entry(self.pro_table)        
        manufacor.place(x=394,y=10)

        #phone_number
        Label(self.pro_table, text = "Phone Number",bg='#FBFAFC').place(x =595, y = 10)
        price = Entry(self.pro_table)
        price.place(x=700,y=10)

        self.send_to_database_search_product = partial(self.send_to_database_search_product,name, manufacor, price)
        save = Button(self.pro_table,command=self.send_to_database_search_product, text = "Search").place(x =900, y =6)
    

    def get_data(self):
        return self.primary_add_data()
    
    def get_var_1(self,event):
        value = self.cb1_var.get()
        self.cb2.config(values=self.tools_option[value])

    def create_combox(self,x1,y1,x2,y2):

        self.frame = Frame(self.root, width =178, height = 20,bg='#fff')
        self.frame.place(x=x1,y=y1)
        cb1_values = list(self.tools_option.keys())

        self.cb1_var = StringVar()
        self.cb1_var.set('select item')
        self.cb1 = ttk.Combobox(self.frame, values=cb1_values, textvariable=self.cb1_var)
        self.cb1.place(x=0,y=0)
        self.cb1.bind('<<ComboboxSelected>>', self.get_var_1)


        self.frame2 = Frame(self.root, width =178, height = 20,bg='#fff')
        self.frame2.place(x=x2,y=y2)
        self.cb2_var = StringVar()
        self.cb2_var.set('...')
        self.cb2 = ttk.Combobox(self.frame2, values=self.tools_option[cb1_values[0]], textvariable=self.cb2_var)           
        self.cb2.place(x=0,y=0)
        
    def add_product(self):

        self.start()               
        #combox
        self.create_combox(100,91,400,291)

        #title window
        Label(self.root, text='Welcom to Page Register Product',bg='#FBFAFC').pack(pady=10)
        
        #type
        Label(self.root, text ="Type",bg='#FBFAFC').place(x=100,y=70)
        type_tool = self.cb1

        #brand
        Label(self.root, text ="Brand",bg='#FBFAFC').place(x=400,y=70)
        brand = Entry(self.root)        
        brand.place(x=400,y=90,width=157)

        #manufactor
        Label(self.root, text = "Manufactor",bg='#FBFAFC').place(x = 100, y = 140)
        manufactor = Entry(self.root)
        manufactor.place(x=100,y=160)

        #number_of_product
        Label(self.root, text = "Number of Product",bg='#FBFAFC').place(x = 400, y = 140)
        number_of_product = Entry(self.root,)
        number_of_product.place(x=400,y=160)

        #color
        Label(self.root, text = "Name",bg='#FBFAFC').place(x = 100, y = 210)
        name = Entry(self.root)
        name.place(x=100,y=230)

        #price
        Label(self.root, text = "Price",bg='#FBFAFC').place(x = 400, y = 210)
        price = Entry(self.root)
        price.place(x=400,y=230,width=157)

        #status
        Label(self.root, text = "Staus",bg='#FBFAFC').place(x = 100, y = 270)
        status = Entry(self.root,fg='blue')
        status.place(x=100,y=290)

        #cat_type
        Label(self.root, text = "Cat_type",bg='#FBFAFC').place(x = 400, y = 270)
        cat_type = self.cb2
        
        #Register
        self.send_to_database = partial(self.send_to_database,type_tool,brand,name,manufactor,cat_type,price,status,number_of_product)
        Button(self.root, text = "Register",command=self.send_to_database).place(x =294, y = 355)

        self.root.mainloop()
        