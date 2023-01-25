from tkinter import Tk,Entry,Button,Label,Toplevel,Menu,Frame,ttk,Scrollbar
from functools import partial
from costumer import costumer_
from Database_Connect import database

class main:
    
    def __init__(self):
        self.top = Tk()
        self.top.title('Welcom to Main Page')
        self.top.geometry('1300x800')
        self.top.resizable(0,0) 
        self.top.config(bg='#FBFAFC')
        #menu
        self.menubar = Menu(self.top) 
        #fram table
        main_frame = Frame(self.top)
        main_frame.pack(padx=0,pady=0)
        #scrollbar
        scroll = Scrollbar(main_frame)
        scroll.pack(side='right', fill='y')
        #table
        self.my_table = ttk.Treeview(main_frame,yscrollcommand=scroll.set)
        self.my_table.config(height=35)
        scroll.config(command=self.my_table.yview)
        
    def costumer_start(self):
        costumer_.main_costumer()

    def products(self):
        pass

    def factors(self):
        pass

    def payments(self):
        pass

    def menu(self):
        self.add = Menu(self.menubar, tearoff=0)  
        self.add.add_command(label="add costumer")  
        self.add.add_command(label="add product")    
        
        # file.add_command(label="Exit", command=top.quit)  
        
        self.menubar.add_cascade(label="   add", menu=self.add)  
        self.search = Menu(self.menubar, tearoff=0)   
        
        
        self.search.add_command(label="costumers",command=self.costumer_start)  
        self.search.add_command(label="products")  
        self.search.add_command(label="factors")  
        self.search.add_command(label="payments")  
        
        self.menubar.add_cascade(label="  search", menu=self.search)  
        help = Menu(self.menubar, tearoff=0)  
        help.add_command(label="About")  
        self.menubar.add_cascade(label="Help", menu=help)  
        
        self.top.config(menu=self.menubar)

    def table(self):

        #define our column
        self.my_table['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city','player_city1')
        # format our column
        self.my_table.column("#0", width=0,  stretch='no')
        self.my_table.column("player_id",anchor='center', width=100)
        self.my_table.column("player_name",anchor='center',width=100)
        self.my_table.column("player_Rank",anchor='center',width=100)
        self.my_table.column("player_states",anchor='center',width=100)
        self.my_table.column("player_city",anchor='center',width=100)
        self.my_table.column("player_city1",anchor='center',width=100)
        # Create Headings 
        self.my_table.heading("#0",text="",anchor='center')
        self.my_table.heading("player_id",text="Id",anchor='center')
        self.my_table.heading("player_name",text="Name",anchor='center')
        self.my_table.heading("player_Rank",text="Rank",anchor='center')
        self.my_table.heading("player_states",text="States",anchor='center')
        self.my_table.heading("player_city",text="States",anchor='center')

        # add data 
        database.set_query('CALL get_costumer();',)
        data = database.connect()
        for i in range(len(data)):
            self.my_table.insert(parent='',index='end',iid=i,text='',
            values=data[i])
        
        self.my_table.pack()
        self.my_table.mainloop() 


    def show(self):
        self.menu()
        self.table()
        


if __name__ == "__main__":
    main().show()