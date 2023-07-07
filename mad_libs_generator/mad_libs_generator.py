import tkinter as tk

class principal_window :
    def __init__(self) :
        self.root = tk.Tk()
        self.root.title("Mad Libs Genarator")
        self.root.geometry("400x200")
        self.label1= tk.Label(self.root , text="Mad Libs Game" , font=("Italic" , 30) , foreground="blue")
        self.label1.pack(padx=10 )

        self.label2= tk.Label(self.root , text="Choose Your Favorite Story :" , font=("Bold", 20) , background="yellow" , foreground="black")
        self.label2.pack(padx=10 , pady=10)

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0 , weight=1)
        self.buttonFrame.columnconfigure(1 , weight=1)
        self.buttonFrame.columnconfigure(2 , weight=1)
        
        self.btn1 = tk.Button(self.buttonFrame , text="Story 1" , font=("Arial" , 16) , command=self.show_Entry_window_1)
        self.btn1.grid(row=0 , column=0 , sticky=tk.W+tk.E)

        self.btn2 = tk.Button(self.buttonFrame , text=("Story 2") , font=("Arial" , 16) ,  command=self.show_Entry_window_2)
        self.btn2.grid(row=0 , column=1 ,sticky=tk.W+tk.E)
        self.btn3 = tk.Button(self.buttonFrame , text="Story 3" , font=("Arial" , 16) , command=self.show_Entry_window_3)
        self.btn3.grid(row=0 , column=2 , sticky=tk.W+tk.E)
        self.buttonFrame.pack(fill="both")

        self.root.mainloop()

    def show_Entry_window_1(self):
        root = tk.Tk()
        root.title("story")
        root.geometry("300x200")

        button_enter_Frame = tk.Frame(root)
        button_enter_Frame.columnconfigure(0 , weight=1)
        button_enter_Frame.columnconfigure(1 , weight=1)

        global textEnter11 , textEnter21 , textEnter31 , textEnter41 , textEnter51 , textEnter61
        label1 = tk.Label(button_enter_Frame , text="enter adjective :" , font="Arial")
        label1.grid(row=0 , column=0 , sticky=tk.W+tk.E)
        textEnter11 = tk.Entry(button_enter_Frame)
        textEnter11.grid(row=0 , column=1 , sticky=tk.W+tk.E)
       
        label2 = tk.Label(button_enter_Frame , text="enter a preson name :" , font="Arial")
        label2.grid(row=1 , column=0 , sticky=tk.W+tk.E)
        textEnter21 = tk.Entry(button_enter_Frame)
        textEnter21.grid(row=1 , column=1 , sticky=tk.W+tk.E)

        label3 = tk.Label(button_enter_Frame , text="enter a thing name :" , font="Arial")
        label3.grid(row=2 , column=0 , sticky=tk.W+tk.E)
        textEnter31 = tk.Entry(button_enter_Frame)
        textEnter31.grid(row=2 , column=1 , sticky=tk.W+tk.E)

        label41 = tk.Label(button_enter_Frame , text="enter a place name :" , font="Arial")
        label41.grid(row=3 , column=0 , sticky=tk.W+tk.E)
        textEnter41 = tk.Entry(button_enter_Frame)
        textEnter41.grid(row=3 , column=1 , sticky=tk.W+tk.E)

        label51 = tk.Label(button_enter_Frame , text="enter a food name :" , font="Arial")
        label51.grid(row=4 , column=0 , sticky=tk.W+tk.E)
        textEnter51 = tk.Entry(button_enter_Frame)
        textEnter51.grid(row=4 , column=1 , sticky=tk.W+tk.E)

        label61 = tk.Label(button_enter_Frame , text="enter a verb name :" , font="Arial")
        label61.grid(row=5 , column=0 , sticky=tk.W+tk.E)
        textEnter61 = tk.Entry(button_enter_Frame)
        textEnter61.grid(row=5 , column=1 , sticky=tk.W+tk.E)
        button_enter_Frame.pack()

        button = tk.Button(root , text="Submit" , font=("Arial" , 18) , command=self.Text_show_window_1)
        button.pack()

        root.mainloop()
    def show_Entry_window_2(self):
        root = tk.Tk()

        root.title("story")
        root.geometry("300x200")

        button_enter_Frame = tk.Frame(root)
        button_enter_Frame.columnconfigure(0 , weight=1)
        button_enter_Frame.columnconfigure(1 , weight=1)

        global textEnter12 , textEnter22 , textEnter32 , textEnter42 , textEnter52 , textEnter62
        label1 = tk.Label(button_enter_Frame , text="enter adjective :" , font="Arial")
        label1.grid(row=0 , column=0 , sticky=tk.W+tk.E)
        textEnter12 = tk.Entry(button_enter_Frame)
        textEnter12.grid(row=0 , column=1 , sticky=tk.W+tk.E)

        label2 = tk.Label(button_enter_Frame , text="enter a preson name :" , font="Arial")
        label2.grid(row=1 , column=0 , sticky=tk.W+tk.E)
        textEnter22 = tk.Entry(button_enter_Frame)
        textEnter22.grid(row=1 , column=1 , sticky=tk.W+tk.E)

        label3 = tk.Label(button_enter_Frame , text="enter a thing name :" , font="Arial")
        label3.grid(row=2 , column=0 , sticky=tk.W+tk.E)
        textEnter32 = tk.Entry(button_enter_Frame)
        textEnter32.grid(row=2 , column=1 , sticky=tk.W+tk.E)

        label4 = tk.Label(button_enter_Frame , text="enter a place name :" , font="Arial")
        label4.grid(row=3 , column=0 , sticky=tk.W+tk.E)
        textEnter42 = tk.Entry(button_enter_Frame)
        textEnter42.grid(row=3 , column=1 , sticky=tk.W+tk.E)

        label5 = tk.Label(button_enter_Frame , text="enter a food name :" , font="Arial")
        label5.grid(row=4 , column=0 , sticky=tk.W+tk.E)
        textEnter52 = tk.Entry(button_enter_Frame)
        textEnter52.grid(row=4 , column=1 , sticky=tk.W+tk.E)

        label6 = tk.Label(button_enter_Frame , text="enter a verb name :" , font="Arial")
        label6.grid(row=5 , column=0 , sticky=tk.W+tk.E)
        textEnter62 = tk.Entry(button_enter_Frame)
        textEnter62.grid(row=5 , column=1 , sticky=tk.W+tk.E)
        button_enter_Frame.pack()

        button = tk.Button(root , text="Submit" , font=("Arial" , 18) , command=self.Text_show_window_2)
        button.pack()

        root.mainloop()
    
    def show_Entry_window_3(self):
        root = tk.Tk()

        root.title("story")
        root.geometry("300x200")

        button_enter_Frame = tk.Frame(root)
        button_enter_Frame.columnconfigure(0 , weight=1)
        button_enter_Frame.columnconfigure(1 , weight=1)

        global textEnter13 , textEnter23 , textEnter33 , textEnter43 , textEnter53 , textEnter63
        label1 = tk.Label(button_enter_Frame , text="enter adjective :" , font="Arial")
        label1.grid(row=0 , column=0 , sticky=tk.W+tk.E)
        textEnter13 = tk.Entry(button_enter_Frame)
        textEnter13.grid(row=0 , column=1 , sticky=tk.W+tk.E)

        label2 = tk.Label(button_enter_Frame , text="enter a preson name :" , font="Arial")
        label2.grid(row=1 , column=0 , sticky=tk.W+tk.E)
        textEnter23 = tk.Entry(button_enter_Frame)
        textEnter23.grid(row=1 , column=1 , sticky=tk.W+tk.E)

        label3 = tk.Label(button_enter_Frame , text="enter a thing name :" , font="Arial")
        label3.grid(row=2 , column=0 , sticky=tk.W+tk.E)
        textEnter33 = tk.Entry(button_enter_Frame)
        textEnter33.grid(row=2 , column=1 , sticky=tk.W+tk.E)

        label4 = tk.Label(button_enter_Frame , text="enter a place name :" , font="Arial")
        label4.grid(row=3 , column=0 , sticky=tk.W+tk.E)
        textEnter43 = tk.Entry(button_enter_Frame)
        textEnter43.grid(row=3 , column=1 , sticky=tk.W+tk.E)

        label5 = tk.Label(button_enter_Frame , text="enter a food name :" , font="Arial")
        label5.grid(row=4 , column=0 , sticky=tk.W+tk.E)
        textEnter53 = tk.Entry(button_enter_Frame)
        textEnter53.grid(row=4 , column=1 , sticky=tk.W+tk.E)

        label6 = tk.Label(button_enter_Frame , text="enter a verb name :" , font="Arial")
        label6.grid(row=5 , column=0 , sticky=tk.W+tk.E)
        textEnter63 = tk.Entry(button_enter_Frame)
        textEnter63.grid(row=5 , column=1 , sticky=tk.W+tk.E)
        button_enter_Frame.pack()

        button = tk.Button(root , text="Submit" , font=("Arial" , 18) , command=self.Text_show_window_3)
        button.pack()

        root.mainloop()

    def Text_show_window_1(self):
        self.root = tk.Tk()
        self.root.title = "Result"
        self.root.geometry("500x100")
        self.root.grid_columnconfigure(0, weight=1)
        self.LABEL = tk.Label(self.root , text=f'In the bustling city of {textEnter41.get()}, {textEnter21.get()}, a talented artist,\n{textEnter61.get()} solace in her {textEnter31.get()} and palette.\
With a cup of steaming {textEnter11.get()} {textEnter51.get()} by her side,\nshe captured the vibrant energy of Times Square on her canvas,\n\
bringing its lively spirit to life' , font=("Bold") , justify="left")
        self.LABEL.pack(fill="both")
        self.root.mainloop()
        
    def Text_show_window_2(self):
        self.root = tk.Tk()
        self.root.title = "Result"
        self.root.geometry("1150x100")
        self.root.grid_columnconfigure(0, weight=1)
        self.LABEL = tk.Label(self.root , text=f'In the {textEnter12.get()} {textEnter42.get()} town of Seaside, {textEnter22.get()}, an avid surfer,\nembraced the crashing waves with his trusty surfboard, carving graceful arcs along the shimmering turquoise waters.\
 As the salty breeze tousled his sun-kissed hair,\nhe {textEnter62.get()} the freedom of the ocean and savored the tangy freshness of a perfectly ripe {textEnter52.get()},\na tropical delight that {textEnter32.get()} the paradise surrounding him.' , font=("Bold") , justify="left")
        self.LABEL.pack(fill="both")
        self.root.mainloop()
        
    def Text_show_window_3(self):
        self.root = tk.Tk()
        self.root.title = "Result"
        self.root.geometry("700x150")
        self.root.grid_columnconfigure(0, weight=1)
        self.LABEL = tk.Label(self.root , text=f'Deep in the heart of the mystical {textEnter43.get()}Forest,\n{textEnter23.get()}, a fearless explorer,\
embarked on a quest to {textEnter63.get()} the legendary Crystal of Serenity.\n\
With her faithful companion, a shimmering silver {textEnter33.get()}, she ventured through the ancient trees,\n\
guided by the {textEnter13.get()} glow of fireflies.\nIn a hidden glade, she discovered a {textEnter53.get()} fit for royalty,\n\
a mouthwatering banquet of succulent roasted lamb, tender and bursting with flavor,\nthat replenished her \
strength for the challenges that lay ahead.' , font=("Bold") , justify="left")
        self.LABEL.pack(fill="both")
        self.root.mainloop()

principal_window()