# import tkinter as tk  
# from functools import partial  
   
   
# def call_result(label_result, n1, n2):  
#     num1 = (n1.get())  
#     num2 = (n2.get())  
#     label_result.config(text="Result = %d" % num1)  
#     return  
   
# root = tk.Tk()  
# root.geometry('400x200+100+200')  
  
# root.title('Calculator')  
   
# number1 = tk.StringVar()  
# number2 = tk.StringVar()  
  
# tk.Label(root, text="name").place(x=30, y=5)  
  
# tk.Label(root, text="last").place(x=30, y=20)  
  
# labelResult = tk.Label(root)  
  
# labelResult.grid(row=7, column=2)  
  
# entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
# entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
# call_result = partial(call_result, labelResult, number1, number2)  
  
# buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)  
  
# root.mainloop()
# sql = "CALL Register_costumer(%s,%s,%s,%s,%s,%s);"
# val = ("John", "nnn",'hh','09387145655','email_l')
# print(sql,val)
#Costumers
        # Label(text='                                     ', bg='#FBFAFC').grid(row=0, column=0)
        # Button(self.root, text = "Costumers",command=self.costumer_start).grid(row=2,column=1,pady=10)
        # #Products
        # Button(self.root, text = "Products   ",command=self.products).grid(row=4,column=1,pady=15)
        # #Factors
        # Button(self.root, text = "Factors    ",command=self.payments).grid(row=6,column=1,pady=15)
        # #Payments
        # Button(self.root, text = "Payments ",command=self.payments).grid(row=8,column=1,pady=15)

        # Label(text='Please select any one ;)', bg='#FBFAFC').grid(row=9, column=1,pady=5)

        # #loop
        # self.root.mainloop()
# from tkinter import Toplevel, Button, Tk, Menu  
  
# top = Tk()
# top.geometry('1300x800')  
# menubar = Menu(top)  
# add = Menu(menubar, tearoff=0)  
# file.add_command(label="add costumer")  
# file.add_command(label="add product")  
# # file.add_command(label="Save")  
# # file.add_command(label="Save as...")  
# # file.add_command(label="Close")  
  
# file.add_separator()  
  
# file.add_command(label="Exit", command=top.quit)  
  
# menubar.add_cascade(label="add", menu=file)  
# edit = Menu(menubar, tearoff=0)  
# edit.add_command(label="Undo")  
  
# edit.add_separator()  
  
# edit.add_command(label="Cut")  
# edit.add_command(label="Copy")  
# edit.add_command(label="Paste")  
# edit.add_command(label="Delete")  
# edit.add_command(label="Select All")  
  
# menubar.add_cascade(label="search", menu=edit)  
# help = Menu(menubar, tearoff=0)  
# help.add_command(label="About")  
# menubar.add_cascade(label="Help", menu=help)  
  
# top.config(menu=menubar)  
# top.mainloop() 
# from tkinter import *
 
 
# class Table:
     
#     def __init__(self,root):
         
#         # code for creating table
#         for i in range(total_rows):
#             for j in range(total_columns):
                 
#                 self.e = Entry(root, width=20, fg='blue',
#                                font=('Arial',16,'bold'))
                 
#                 self.e.grid(row=i, column=j)
#                 self.e.insert(END, lst[i][j])
 
# # take the data
# lst = [(1,'Raj','Mumbai',19),
#        (2,'Aaryan','Pune',18),
#        (3,'Vaishnavi','Mumbai',20),
#        (4,'Rachna','Mumbai',21),
#        (5,'Shubham','Delhi',21)]
  
# # find total number of rows and
# # columns in list
# total_rows = len(lst)
# total_columns = len(lst[0])
  
# # create root window
# root = Tk()
# t = Table(root)
# root.mainloop()
# import tkinter as tk

# import tksheet

# top = tk.Tk()

# sheet = tksheet.Sheet(top,show_top_left=False,)

# sheet.grid()

# sheet.set_sheet_data([[f"{ri+cj}" for cj in range(8)] for ri in range(4)])


# # table enable choices listed below:

# sheet.enable_bindings(("single_select",

#                        "row_select",

#                        "column_width_resize",

#                        "arrowkeys",

#                        "right_click_popup_menu",

#                        "rc_select",

#                        "rc_insert_row",

#                        "rc_delete_row",

#                        "copy",

#                        "cut",

#                        "paste",

#                        "delete",

#                        "undo",

#                        "edit_cell"))

# top.mainloop()

# from tkinter import *
# from  tkinter import ttk


# ws  = Tk()
# ws.title('PythonGuides')
# ws.geometry('300x400')

# set = ttk.Treeview(ws)
# set.pack(side=TOP)

# set['columns']= ('id', 'full_Name','award')
# set.column("#0", width=0,  stretch=NO)
# set.column("id",anchor=CENTER, width=80)
# set.column("full_Name",anchor=CENTER, width=80)
# set.column("award",anchor=CENTER, width=80)

# set.heading("#0",text="",anchor=CENTER)
# set.heading("id",text="ID",anchor=CENTER)
# set.heading("full_Name",text="Full_Name",anchor=CENTER)
# set.heading("award",text="Award",anchor=CENTER)

# set.insert(parent='',index='end',iid=0,text='',
# values=('101','john','Gold'))
# set.insert(parent='',index='end',iid=1,text='',
# values=('102','jack',"Silver"))
# set.insert(parent='',index='end',iid=2,text='',
# values=('103','joy','Bronze'))

# ws.mainloop()
# from tkinter import *
# from  tkinter import ttk


# ws  = Tk()
# ws.title('PythonGuides')
# ws.geometry('500x500')
# ws['bg'] = '#AC99F2'

# game_frame = Frame(ws)
# game_frame.pack(padx=0,pady=0)

# #scrollbar
# game_scroll = Scrollbar(game_frame)
# game_scroll.pack(side=RIGHT, fill=Y)

# # game_scroll = Scrollbar(game_frame,orient='horizontal')
# # game_scroll.pack(side= BOTTOM,fill=X)

# my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set)


# my_game.pack(padx=0,pady=0)

# game_scroll.config(command=my_game.yview)
# game_scroll.config(command=my_game.xview)

# #define our column
 
# my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city','player_city1')

# # format our column
# my_game.column("#0", width=0,  stretch=NO)
# my_game.column("player_id",anchor=CENTER, width=100)
# my_game.column("player_name",anchor=CENTER,width=100)
# my_game.column("player_Rank",anchor=CENTER,width=100)
# my_game.column("player_states",anchor=CENTER,width=100)
# my_game.column("player_city",anchor=CENTER,width=100)
# my_game.column("player_city1",anchor=CENTER,width=100)
# # Create Headings 
# my_game.heading("#0",text="",anchor=CENTER)
# my_game.heading("player_id",text="Id",anchor=CENTER)
# my_game.heading("player_name",text="Name",anchor=CENTER)
# my_game.heading("player_Rank",text="Rank",anchor=CENTER)
# my_game.heading("player_states",text="States",anchor=CENTER)
# my_game.heading("player_city",text="States",anchor=CENTER)

# # #add data 

# my_game.insert(parent='',index='end',iid=1,text='',
# values=('2','Ranger','102','Wisconsin', 'Green Bay'))

# my_game.pack()


# ws.mainloop()
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Checkbox Demo')

# agreement = tk.StringVar()


# def agreement_changed():
#     tk.messagebox.showinfo(title='Result',
#                         message=agreement.get())


# ttk.Checkbutton(root,
#                 text='I agree',
#                 command=agreement_changed,
#                 variable=agreement,
#                 onvalue='agree',
#                 offvalue='disagree').pack()


# root.mainloop()

# import tkinter as tk
# from tkinter import ttk


# class App(tk.Tk):
    
#     def __init__(self):
#         super().__init__()

#         self.geometry('300x250')
#         self.title('Menubutton Demo')

#         # self.create_menu_button()

#     def create_menu_button(self):
#         """ create a menu button """
#         # menu variable
#         colors = ('Red', 'Green', 'Blue')

#         # create the Menubutton
#         menu_button = ttk.Menubutton(
#             self,
#             text='Select')

#         # create a new menu instance
#         menu = tk.Menu(menu_button, tearoff=0)

#         for color in colors:
#             menu.add_radiobutton(
#                 label=color,
#                 value=color
#                )

#         # associate menu with the Menubutton
#         menu_button["menu"] = menu

#         menu_button.pack()


# if __name__ == "__main__":
#     app = App()
#     app.create_menu_button()
#     app.mainloop()
# from tkinter import *
 
# root = Tk()
# root.geometry("200x150")
# frame = Frame(root)
# frame.pack()
 
# MenuBttn = Menubutton(frame, text = "Favourite food", relief = RAISED)
 
# Var1 = IntVar()
# Var2 = IntVar()
# Var3 = IntVar()
 
# Menu1 = Menu(MenuBttn, tearoff = 0)
 
# Menu1.add_checkbutton(label = "Pizza", variable = Var1)
# Menu1.add_checkbutton(label = "Cheese Burger", variable = Var2)
# Menu1.add_checkbutton(label = "Salad", variable = Var3)
# print(Menu1.clipboard_get())
# MenuBttn["menu"] = Menu1
 
# MenuBttn.pack()
# root.mainloop()

# import tkinter as tk
# from tkinter import ttk


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.geometry('300x250')
#         self.title('Menubutton Demo')

#         # Menubutton variable
#         self.select_item = tk.StringVar()
#         self.select_item.trace("w", self.menu_item_selected)

#         # create the menu button
#         self.create_menu_button()

#     def menu_item_selected(self, *args):
#         """ handle menu selected event """
#         print(self.select_item.get())

#     def create_menu_button(self):
#         """ create a menu button """
#         # menu variable
#         items = ('Red', 'Green', 'Blue')

#         # create the Menubutton
#         menu_button = ttk.Menubutton(
#             self,
#             text='Select a color')

#         # create a new menu instance
#         menu = tk.Menu(menu_button, tearoff=0)

#         for item in items:
#             menu.add_radiobutton(
#                 label=item,
#                 value=item,
#                 variable=self.select_item)

#         # associate menu with the Menubutton
#         menu_button["menu"] = menu

#         menu_button.pack(expand=True)


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
# from tkinter import *
# from tkinter import ttk
 
# root = Tk()
# root.geometry("200x150")
 
# frame = Frame(root)
# frame.place(x=100,y=10,width=20)
 
# vlist = ["Option1", "Option2", "Option3",
#           "Option4", "Option5"]

# r = StringVar()
# Combo = ttk.Combobox(frame, values = vlist)
# Combo.set("Pick an Option")
# Combo.place(x=20,y=10)
# # print(r.get())

# root.mainloop()
import tkinter as tk
from tkinter import ttk
 
class Window:
    def __init__(self, root):
        self.root = root
 
        # Frame
        self.frame = tk.Frame(self.root, width = 200, height = 200)
        self.frame.pack()
 
        self.vlist = ["Option1", "Option2", "Option3", "Option4", "Option5"]
 
        self.combo = ttk.Combobox(self.frame, values = self.vlist, state = "readonly")
        self.combo.set("Pick an Option")
        self.combo.place(x = 20, y = 50)
 
 
root = tk.Tk()
root.title("Tkinter")
 
window = Window(root)
root.mainloop()