from tkinter import Tk,Entry,Button,Label,ttk,Menu,StringVar,Menubutton,Frame
from functools import partial

class Product:
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Product')
        self.root.geometry('670x400')
        self.root.config(bg='#FBFAFC')
        self.root.resizable(0,0)
        
    
        
        # create the menu button
        # self.create_menu_button()

    def save(self):
        print('save')

    
    def send_to_database(self,type_tool,brand,name,manufactor,cat_type,price,status):

        #get_information
        self.type_tool = type_tool.get()
        self.brand = brand.get()
        self.manufactor = manufactor.get()
        self.name = name.get()
        self.cat_type = cat_type.get()
        self.price = price.get()
        self.status = status.get()

        #send to database
        # database.set_query("CALL Register_product(%s,%s,%s,%s,%s);",(self.brand,self.type_tool))

        # database.connect()
        
        # database.set_query("CALL Register_category(%s,%s,%s,%d,%s);", 
        #                         (self.manufactor,
        #                          self.name,self.cat_type,self.price,self.status))

        # database.connect()
        #reset entery
        brand.delete(0,'end')
        type_tool.delete(0,'end')
        manufactor.delete(0,'end')
        name.delete(0,'end')
        cat_type.delete(0,'end')
        price.delete(0,'end')
        status.delete(0,'end')
    
    def menu_item_selected(self, *args):
        """ handle menu selected event """
        Label(self.root,text=self.select_item.get(),bg='#fff',relief="solid").place(x=100,y=90)


    def create_menu_button(self,arg_tuple=None,x=10,y=10):
        self.select_item = StringVar()
        self.select_item.trace("w", self.menu_item_selected)

        """ create a menu button """
        # menu variable
        items = ('Red', 'Green', 'Blue')

        # create the Menubutton
        menu_button = Menubutton(self.root,text='Select')
        # menu_button1 = Menubutton(self.root,text='Select')

        # create a new menu instance
        menu = Menu(menu_button, tearoff=0)
        # menu1 = Menu(menu_button1,tearoff=0)

        for item in items:
            menu.add_radiobutton(
                label=item,
                value=item,
                variable=self.select_item)
        
        # for item in items:
        #     menu1.add_radiobutton(
        #         label=item,
        #         value=item,
        #         variable=self.select_item)

        # associate menu with the Menubutton
        menu_button["menu"] = menu
        # menu_button1["menu"] = menu1
        #place_menu_button
        menu_button.place(x=x,y=y)
        # menu_button1.place(x=x,y=y+20)
        menu_button.mainloop()

    def create_combox(self,vlist,x,y):
        self.frame = Frame(self.root, width =178, height = 20,bg='#fff')
        self.frame.place(x=x,y=y)
 
        self.vlist = vlist
 
        self.combo = ttk.Combobox(self.frame, values = self.vlist,background='#fff')
        self.combo.set("Pick an Option")
        self.combo.place(x =0,y=0)
        

    def add_product(self):
                       
        #title window
        Label(self.root, text='Welcom to Page Register Product',bg='#FBFAFC').pack(pady=10)
        
        #type
        Label(self.root, text ="Type",bg='#FBFAFC').place(x=100,y=70)
        self.create_combox()
        
        
        
        #brand
        Label(self.root, text ="Brand",bg='#FBFAFC').place(x=400,y=70)
        brand = Entry(self.root)        
        brand.place(x=400,y=90,width=157)

        #manufactor
        Label(self.root, text = "Manufactor",bg='#FBFAFC').place(x = 100, y = 140)
        manufactor = Entry(self.root,width=57)
        manufactor.place(x=100,y=160)

        #color
        Label(self.root, text = "Name",bg='#FBFAFC').place(x = 100, y = 210)
        name = Entry(self.root,fg='blue')
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
        cat_type = Entry(self.root)
        cat_type.place(x=400,y=290,width=157)
        
        
        # self.send_to_database = partial(self.send_to_database,type_tool,brand,name,manufactor,price,status,cat_type)
        # save = Button(self.root, text = "Register",command=self.send_to_database).place(x =294, y = 355)

        

        self.root.mainloop()
        # self.create_menu_button(x=190,y=90)
        # self.create_menu_button(x=100,y=310)

product = Product()
product.add_product()