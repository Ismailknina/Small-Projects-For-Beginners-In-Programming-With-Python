import tkinter as tk
from tkinter import messagebox
import random
import time

class principal_Window :
    def __init__(self) :
        self.root = tk.Tk()
        
        self.root.title("Guessing number Game")

        self.root.geometry("500x305")

        self.root.configure(background="White")

        self.label1 = tk.Label(self.root , text="Guessing number Game" , font=("Bold" , 30) , background="White" , foreground= "red")
        self.label1.pack(padx=10 , pady=10)

        self.label2 = tk.Label(self.root , text="Click 'Start' to play :" , font=("ITALIC" , 25))
        self.label2.pack(padx=10 , pady=10)

        self.button1 = tk.Button(self.root , text="Start" , font=("Arial" , 18) ,padx=20 , pady=20 , background="yellow" , command=self.start_main_window )
        self.button1.pack(fill="x")

        self.button2 = tk.Button(self.root , text="Exit" , font=("Arial" , 18) ,padx=20 , pady=20 , background="Purple" , command=self.close_main_window)
        self.button2.pack(fill="x")

        self.root.mainloop()
    
    def close_main_window(self):
        if messagebox.askyesno(message="Do you really want's to leave ?"):
            self.root.destroy()

    def start_main_window(self):
        self.attempts = 7 ; self.trying = 0

        self.The_number_value = random.randrange(1,20)

        self.root1 = tk.Tk()

        self.label3 = tk.Label(self.root1 , text="Enter Your Guessing Number:" , font=("Arial" ,  18))
        self.label3.pack(padx=10 , pady=10)

        self.entry = tk.Entry(self.root1 , font=5 )
        self.entry.pack(padx=10 , pady=10)

        self.button3 = tk.Button(self.root1 , text="Submit" , font=("Arial" , 18) , command=self.checking_ansewr)
        self.button3.pack(padx=10 , pady=10)

        self.label4 = tk.Label(self.root1 , text="Result :" , font=("Bold" , 20) , foreground="Blue" ,)
        self.label4.pack()

        self.label5 = tk.Label(self.root1 , text="" )
        self.label5.pack()

        self.root1.mainloop()
    def checking_ansewr(self):
        if int(self.entry.get()) == self.The_number_value :
            self.label5 = tk.Label(self.root1 , text="You are right" , font=("Arial" ,25) , foreground="Green" , background="White")
            self.label5.pack()

        elif int(self.entry.get()) < self.The_number_value :
            if self.trying == self.attempts :
                    self.root.destroy()
                    self.label5 = tk.Label(self.root1 , text="Sorry You reached the max of attempts!" , font=("Arial" ,30) , foreground="Purple" , background="White")
                    self.label5.pack()
                    time.sleep(1.5)
                    if messagebox.askyesno(message="You want to end the Game ?"):
                         self.root1.destroy()   
                    else :
                        self.root1.destroy()
                        principal_Window()

            else :
                self.label5 = tk.Label(self.root1 , text="It's smaller" , font=("Arial" ,25) , foreground="Red" , background="White")
                self.label5.pack()
                self.button4 = tk.Button(self.root1 , text="Try again" , font=("Arial" , 18) , command=self.clearing_the_entry)
                self.button4.pack(padx=10 , pady=10)
                self.trying += 1

        elif int(self.entry.get()) > self.The_number_value :
            if self.trying == self.attempts :
                    self.root.destroy()
                    self.label5 = tk.Label(self.root1 , text="Sorry You reached the max of attempts!" , font=("Arial" ,30) , foreground="Purple" , background="White")
                    self.label5.pack()
                    time.sleep(1.5)
                    if messagebox.askyesno(message="You want to end the Game ?"):
                         self.root1.destroy()
                    else :
                        self.root1.destroy()
                        principal_Window()
                    
            else :
                self.label5 = tk.Label(self.root1 , text="It's Biger" , font=("Arial" ,25) , foreground="red" , background="White")
                self.label5.pack()
                self.button4 = tk.Button(self.root1 , text="Try again" , font=("Arial" , 18) , command=self.clearing_the_entry)
                self.button4.pack(padx=10 , pady=10)
                self.trying += 1

    def clearing_the_entry(self):
        self.entry.delete(0 ,'end')
        self.label5.destroy()
        self.button4.destroy()
    
principal_Window()