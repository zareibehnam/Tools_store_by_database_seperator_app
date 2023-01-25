from tkinter import Tk,Entry,Button,Label
from functools import partial
from Database_Connect import database

class Costumer:
    
    def __init__(self):
        pass

    def save(self):
        pass

    
    def send_to_database(self,name,Lastname,phone_number,address,email):

        #get_information
        self.name = name.get()
        self.lastname = Lastname.get()
        self.address = address.get()
        self.phone_number = phone_number.get()
        self.email = email.get()

        #send to database
        database.set_query("CALL Register_costumer(%s,%s,%s,%s,%s);", 
                                (self.name,
                                 self.lastname,self.address,
                                 self.phone_number,self.email))

        database.connect()
        
        #reset entery
        name.delete(0,'end')
        Lastname.delete(0,'end')
        address.delete(0,'end')
        phone_number.delete(0,'end')
        email.delete(0,'end')

    def add_costumer(self):
        
        root = Tk()
        root.title('Costumer')
        root.geometry('670x400')
        root.config(bg='#FBFAFC')
        root.resizable(0,0)
        
        #title window
        Label(root, text='Welcom to page Register Costumer',bg='#FBFAFC').pack(pady=10)

        #name
        Label(root, text ="First Name",bg='#FBFAFC').place(x=100,y=70)
        name = Entry(root)        
        name.place(x=100,y=100)
        
        #lastname
        Label(root, text ="LastName",bg='#FBFAFC').place(x=400,y=70)
        Lastname = Entry(root)        
        Lastname.place(x=400,y=100,width=157)

        #address
        Label(root, text = "Address",bg='#FBFAFC').place(x = 100, y = 140)
        address = Entry(root,width=57)
        address.place(x=100,y=170)

        #phone_number
        Label(root, text = "Phone Number",bg='#FBFAFC').place(x = 100, y = 230)
        phone_number = Entry(root,fg='blue')
        phone_number.place(x=100,y=250)

        #email
        Label(root, text = "Email",bg='#FBFAFC').place(x = 400, y = 230)
        email = Entry(root)
        email.place(x=400,y=250,width=157)
        
        
        self.send_to_database = partial(self.send_to_database,name,Lastname,phone_number,address,email)
        save = Button(root, text = "Register",command=self.send_to_database,bg='blue').place(x =285, y = 330)

        #loop
        root.mainloop()



costumer_ = Costumer()