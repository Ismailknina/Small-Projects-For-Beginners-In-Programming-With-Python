import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

os.chdir(r"c:\elzero\python\Python_Projects\gareeb_pyproject")
class Home_Window:
    def __init__(self) :
        self.root = tk.Tk()

        self.root.title("Contact Book")

        self.root.geometry("700x200")

        self.root.configure(background="White" )

        self.label = tk.Label(self.root , text="Welcome to IK Contact Book" , font=("Bold " , 35) , background="red" , foreground="White" )
        self.label.pack(padx=10 , pady=10)


        self.buttonFrame = tk.Frame(self.root , background="white")
        self.buttonFrame.columnconfigure(0 , weight=1)
        self.buttonFrame.columnconfigure(1 , weight=1)
        self.buttonFrame.columnconfigure(2 , weight=1)

        self.button1 = tk.Button(self.buttonFrame , text="Add" , foreground="White" , background="Blue" , font=("ITALIC" ,20) , width=10 , command=self.Add)
        self.button1.grid(row=0 , column=0)

        self.button2 = tk.Button(self.buttonFrame , text="View" , foreground="White" , background="Blue" , font=("ITALIC" ,20),width=10 , command=self.view)
        self.button2.grid(row=0 , column=1)

        self.button3 = tk.Button(self.buttonFrame , text="Delete" , foreground="White" , background="Blue" , font=("ITALIC" ,20),width=10 , command=self.delete_principale)
        self.button3.grid(row=0 , column=2)        

        self.button4 = tk.Button(self.buttonFrame , text="Edit" , foreground="White" , background="Blue" , font=("ITALIC" ,20),width=10 , command=self.Edit_principale)
        self.button4.grid(row=1 , column=0)

        self.button5 = tk.Button(self.buttonFrame , text="Reset" , foreground="White" , background="Blue" , font=("ITALIC" ,20),width=10 , command=self.Reset)
        self.button5.grid(row=1 , column=1)

        self.button6 = tk.Button(self.buttonFrame , text="Exit" , foreground="White" , background="black" , font=("ITALIC" ,20),width=10 , command=self.Exit)
        self.button6.grid(row=1 , column=2)

        self.buttonFrame.pack(fill="x")

        self.root.mainloop()


    
    def Add(self):
        global rootAdd
        rootAdd = tk.Tk()

        rootAdd.configure(background="white")


        entryFrame = tk.Frame(rootAdd , background='white')

        entryFrame.columnconfigure(0 , weight=1)
        entryFrame.columnconfigure(1 , weight=1)

        global entryFN , entrySN , entryNumber , entryCOMAPNY  , entryEmail

        labelFN = tk.Label(entryFrame , font=("Bold" , 20) , background='white' , foreground="black" , text="First Name:" )
        labelFN.grid(row=0 , column=0 , sticky=tk.E + tk.W)       

        entryFN = tk.Entry(entryFrame , font=("Arial" , 20) , background='white' , foreground="black" )
        entryFN.grid(row=0 , column=1 , sticky=tk.E + tk.W)

        labelSN = tk.Label(entryFrame , font=("Bold" , 20) , background='white' , foreground="black" , text="Seconde Name:" )
        labelSN.grid(row=1 , column=0 , sticky=tk.E + tk.W)  

        entrySN = tk.Entry(entryFrame , font=("Arial" , 20) , background='white' , foreground="black")
        entrySN.grid(row=1 , column=1 , sticky=tk.E + tk.W)

        labelCompany = tk.Label(entryFrame , font=("Bold" , 20) , background='white' , foreground="black" , text="Company:" )
        labelCompany.grid(row=2 , column=0 , sticky=tk.E + tk.W)  

        entryCOMAPNY = tk.Entry(entryFrame , font=("Arial" , 20) , background='white' , foreground="black")
        entryCOMAPNY.grid(row=2 , column=1 , sticky=tk.E + tk.W)

        labelNumber = tk.Label(entryFrame , font=("Bold" , 20) , background='white' , foreground="black" , text="Phone Number:" )
        labelNumber.grid(row=3 , column=0 , sticky=tk.E + tk.W)  


        entryNumber = tk.Entry(entryFrame , font=("Arial" , 20) , background='white' , foreground="black")
        entryNumber.grid(row=3 , column=1 , sticky=tk.E + tk.W)

        labelEmail = tk.Label(entryFrame , font=("Bold" , 20) , background='white' , foreground="black" , text="Email:" )
        labelEmail.grid(row=4 , column=0 , sticky=tk.E + tk.W)  

        entryEmail = tk.Entry(entryFrame , font=("Arial" , 20) , background='white' , foreground="black")
        entryEmail.grid(row=4 , column=1 , sticky=tk.E + tk.W)

        entryFrame.pack(padx=10 , pady=10)
        

        SumbitButton = tk.Button(rootAdd , text="Sumbit" , font=("Bold" , 25)  , command=self.Sumbit)
        SumbitButton.pack(padx=10 , pady=10)

        rootAdd.mainloop()

    def Sumbit(self): 
        ######################################################################""
        # connection to database
        db = sqlite3.connect("Contact_Books.db")
        # Creating cursor
        cr = db.cursor()
        # Creating Table 
        cr.execute("CREATE TABLE IF NOT EXISTS contact ('first name' TEXT , 'second name' TEXT , 'comapny' TEXT , 'phone number' TEXT , 'email' TEXT)")
        db.commit()
        #cr.execute(f"SELECT 'first name' FROM contact WHERE 'first name' = '{entryFN.get().strip().capitalize()}' and 'second name' = '{entrySN.get().strip().capitalize()}' ")
        # cr.execute("SELECT name FROM user WHERE user_id = 2 ")
        #FN_SN = cr.fetchone()
        #if FN_SN  == None:  # Theres No Skill With This Name In Database
        cr.execute(f"INSERT INTO contact VALUES ('{entryFN.get().strip().capitalize()}','{entrySN.get().strip().capitalize()}','{entryCOMAPNY.get().strip().capitalize()}','{entryNumber.get().strip().capitalize()}','{entryEmail.get().strip().capitalize()}') ")
        #messagebox.showerror(message="Sorry the number or the name of the user are already exists")
            
        db.commit()
        db.close()



    def view(self):
        global rootview
        rootview = tk.Tk()

        rootview.configure(background="white")

        global entrySNV , entryFNV

        labelFN = tk.Label(rootview , font=("Bold" , 20) , background='white' , foreground="black" , text="Enter Name :" )
        labelFN.pack(padx=10 , pady=10)

        entryFNV = tk.Entry(rootview , font=("Arial" , 20) , background='white' , foreground="black" )
        entryFNV.pack(padx=10 , pady=10)

        labelSN= tk.Label(rootview , font=("Bold" , 20) , background='white' , foreground="black" , text="Enter Second name :" )
        labelSN.pack(padx=10 , pady=10)

        entrySNV = tk.Entry(rootview , font=("Arial" , 20) , background='white' , foreground="black" )
        entrySNV.pack(padx=10 , pady=10)

        Search_Button = tk.Button(rootview , font=("Arial" , 20) , background='white' , foreground="black" , text="Search" ,command=self.search )
        Search_Button.pack(padx=10 , pady=10)

        rootview.mainloop()

    def search(self):
        ###########################################################################################################################
        # connection to database
        db = sqlite3.connect("Contact_Books.db")
        # Creating cursor
        cr = db.cursor()
        cr.execute(f'SELECT "phone number" FROM contact WHERE "first name" = "{entryFNV.get().strip().capitalize()}" and "second name" = "{entrySNV.get().strip().capitalize()}" ')
        result = cr.fetchone()
        label_Search= tk.Label(rootview , font=("Bold" , 20) , background='white' , foreground="black" , text=f"Phone number :{result} " ) #
        label_Search.pack(padx=10 , pady=10)
        
        cr.execute(f'SELECT "comapny" FROM contact WHERE "first name" = "{entryFNV.get().strip().capitalize()}" and "second name" = "{entrySNV.get().strip().capitalize()}" ')
        result = cr.fetchone()
        label_Search2= tk.Label(rootview , font=("Bold" , 20) , background='white' , foreground="black" , text=f"Company : {result}" )
        label_Search2.pack(padx=10 , pady=10)
        
        db.commit()
        db.close()
        ############################################################################################################################


        SumbitButton = tk.Button(rootview , text="exit" , font=("Bold" , 25) , command=rootview.destroy)
        SumbitButton.pack(padx=10 , pady=10)

        

    def delete_principale(self):
        global rootdelete
        rootdelete = tk.Tk()

        rootdelete.configure(background="white")

        global entrySND , entryFND

        labelFN = tk.Label(rootdelete , font=("Bold" , 20) , background='white' , foreground="black" , text="Enter Name that's you want's to delete:" )
        labelFN.pack(padx=10 , pady=10)

        entryFND = tk.Entry(rootdelete , font=("Arial" , 20) , background='white' , foreground="black" )
        entryFND.pack(padx=10 , pady=10)

        labelSN= tk.Label(rootdelete , font=("Bold" , 20) , background='white' , foreground="black" , text="Also Enter Second name :" )
        labelSN.pack(padx=10 , pady=10)

        entrySND = tk.Entry(rootdelete , font=("Arial" , 20) , background='white' , foreground="black" )
        entrySND.pack(padx=10 , pady=10)

        Search_Button = tk.Button(rootdelete , font=("Arial" , 20) , background='white' , foreground="black" , text="Delete" ,command=self.delete )
        Search_Button.pack(padx=10 , pady=10)

        rootdelete.mainloop()
        
    def delete(self):
        ###########################################################################################################################
        # connection to database
        db = sqlite3.connect("Contact_Books.db")
        # Creating cursor
        cr = db.cursor()
        cr.execute(f'DELETE FROM contact WHERE "first name" =  "{entryFND.get().strip().capitalize()}" and "second name" = "{entrySND.get().strip().capitalize()}"')
        
        db.commit()
        db.close()
        ############################################################################################################################



        ExitButton = tk.Button(rootdelete , text="exit" , font=("Bold" , 25) , command=rootdelete.destroy)
        ExitButton.pack(padx=10 , pady=10)


    def Edit_principale(self):
        global rootedit
        rootedit = tk.Tk()

        rootedit.configure(background="white")

        global entrySNE , entryFNE , entery_new_phone

        labelFN = tk.Label(rootedit , font=("Bold" , 20) , background='white' , foreground="black" , text="Enter Name that's you want's to Edit:" )
        labelFN.pack(padx=10 , pady=10)

        entryFNE = tk.Entry(rootedit , font=("Arial" , 20) , background='white' , foreground="black" )
        entryFNE.pack(padx=10 , pady=10)

        labelSN= tk.Label(rootedit , font=("Bold" , 20) , background='white' , foreground="black" , text="Also Enter Second name :" )
        labelSN.pack(padx=10 , pady=10)

        entrySNE = tk.Entry(rootedit , font=("Arial" , 20) , background='white' , foreground="black" )
        entrySNE.pack(padx=10 , pady=10)

        labelSNEN= tk.Label(rootedit , font=("Bold" , 20) , background='white' , foreground="black" , text="Put your new phone number:" )
        labelSNEN.pack(padx=10 , pady=10)

        entery_new_phone = tk.Entry(rootedit , font=("Arial" , 20) , background='white' , foreground="black" )
        entery_new_phone.pack(padx=10 , pady=10)

        Search_Button = tk.Button(rootedit , font=("Arial" , 20) , background='white' , foreground="black" , text="Edit" ,command=self.Edit )
        Search_Button.pack(padx=10 , pady=10)

        rootedit.mainloop()

    def Edit(self):
        ###########################################################################################################################
        # connection to database
        db = sqlite3.connect("Contact_Books.db")
        # Creating cursor
        cr = db.cursor()
        cr.execute(f'UPDATE contact SET "phone number" = "{entery_new_phone.get().strip().capitalize()}" WHERE "second name" = "{entrySNE.get().strip().capitalize()}" AND "first name" = "{entryFNE.get().strip().capitalize()}"')
        
        db.commit()
        db.close()
        ############################################################################################################################



        ExitButton = tk.Button(rootedit , text="exit" , font=("Bold" , 25) , command=rootedit.destroy)
        ExitButton.pack(padx=10 , pady=10)


    def Reset(self):
        # if 'normal' == rootview.state():
        #     rootview.destroy()

        # elif 'normal' == rootedit.state():
        #     rootedit.destroy()

        # elif 'normal' == rootdelete.state():
        #     rootdelete.destroy()

        # elif 'normal' == rootAdd.state():
        #     rootAdd.destroy()

        if 'normal' == self.root.state():
            self.root.destroy()
        Home_Window()


    def Exit(self):   
        if messagebox.askyesnocancel(message="Exit ?"):
            self.root.destroy()        

        




Home_Window()