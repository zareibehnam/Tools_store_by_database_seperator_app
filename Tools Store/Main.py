from tkinter import Tk,Entry,Button,Label,Toplevel,Menu,Frame,ttk,Scrollbar
from functools import partial
from Database_Connect import main_database,customer_database,product_database
import customer
import product


class main:
    
    def __init__(self):   
        self.connection()     
        self.top = Tk()
        self.top.title('Welcom to Main Page')
        self.top.geometry('1500x800')
        self.top.resizable(0,0) 
        self.top.config(bg='#FBFAFC')

    def connection(self):
        self.cursor = main_database.connect()
        self.customer = customer.Customer(customer_database.connect())
        self.product = product.Product(product_database.connect())
        
    def customer_add(self):
        self.customer.add_customer()

    def customer_search(self):
        data = self.customer.get_data()
        self.customer.customer_table(data)

    def products_add(self):
        self.product.add_product()

    def product_search(self):
        data = self.product.get_data()
        self.product.product_table(data)


    def factors(self):
        pass

    def payments(self):
        pass

    def menu(self):
        #menu
        self.menubar = Menu(self.top)
        self.add = Menu(self.menubar, tearoff=0)  
        self.add.add_command(label="add customer",command=self.customer_add)  
        self.add.add_command(label="add product",command=self.products_add)    
        
        # file.add_command(label="Exit", command=top.quit)  
        
        self.menubar.add_cascade(label="   add", menu=self.add)  
        self.search = Menu(self.menubar, tearoff=0)   

        self.search.add_command(label="customers",command=self.customer_search)  
        self.search.add_command(label="products",command=self.product_search)  
        self.search.add_command(label="factors")  
        self.search.add_command(label="payments")  
        
        self.menubar.add_cascade(label="  search", menu=self.search)  
        help = Menu(self.menubar, tearoff=0)  
        help.add_command(label="About")  
        self.menubar.add_cascade(label="Help", menu=help)  
        
        self.top.config(menu=self.menubar)

    def table(self,data1):
        #fram table
        main_frame = Frame(self.top,bg='blue')
        main_frame.place(x=0,y=0)

        #scrollbar
        scroll = Scrollbar(main_frame)
        scroll.pack(side='right', fill='y')
        #table
        self.my_table = ttk.Treeview(main_frame,yscrollcommand=scroll.set)
        self.my_table.config(height=35)
        scroll.config(command=self.my_table.yview)
        #define our column
        self.my_table['columns'] = ('customer_name', 'customer_lastname', 'phone_number', 
                                    'product_name', 'price','data','type_payment','status_payment')
        # format our column
        self.my_table.column("#0", width=0,  stretch='no')
        self.my_table.column("customer_name",anchor='center', width=100)
        self.my_table.column("customer_lastname",anchor='center',width=200)
        self.my_table.column("phone_number",anchor='center',width=200)
        self.my_table.column("product_name",anchor='center',width=200)
        self.my_table.column("price",anchor='center',width=200)
        self.my_table.column("data",anchor='center',width=200)
        self.my_table.column("type_payment",anchor='center',width=200)
        self.my_table.column("status_payment",anchor='center',width=200)
        
        # Create Headings 
        self.my_table.heading("#0",text="",anchor='center')
        self.my_table.heading("customer_name",text="name",anchor='center')
        self.my_table.heading("customer_lastname",text="lastname",anchor='center')
        self.my_table.heading("phone_number",text="phone_number",anchor='center')
        self.my_table.heading("product_name",text="product_name",anchor='center')
        self.my_table.heading("price",text="price",anchor='center')
        self.my_table.heading("data",text='data',anchor='center')
        self.my_table.heading("type_payment",text="type_payment",anchor='center')
        self.my_table.heading("status_payment",text="status_payment",anchor='center')
        data = [('behnam','zarei','09387148757','mateh','12000','1400/10/7','cash','not complete!'),
                ('moein','zahmati','09029441787','pichgooshti','50','1400/10/7','creadit','complete')]
        if data != None :
            for i in range(len(data)):
                self.my_table.insert(parent='',index='end',iid=i,text='',values=data[i])

        self.my_table.pack()
        self.my_table.mainloop() 

    def primary_add_data(self):
        sql ="call get_main_information();"
        val = (None)
        self.cursor.execute(sql,val)
        data = self.cursor.fetchall()
        return data
        
    def show(self):
        self.data = self.primary_add_data()
        self.menu()
        self.table(self.data)


if __name__ == "__main__":
    main().show()