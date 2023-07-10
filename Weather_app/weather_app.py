import tkinter as tk
from tkinter import messagebox
import  requests
from PIL import ImageTk, Image


class UI:
    def __init__(self) :
        # Creating window
        self.root = tk.Tk()
        self.root.title("Weather")
        self.root.iconbitmap(r"C:\Users\DELL\Downloads\Wineass-Ios7-Redesign-Weather.ico")
        self.root.configure(background="black")
        self.root.geometry("300x100")
        # Creating Entry where user input the location of city
        self.city_name = tk.StringVar()
        self.entry = tk.Entry(master=self.root  , font=("Bold" , 18) , foreground="Blue" , textvariable=self.city_name).pack(padx=10 , pady=10)
        # Creating search button
        self.button = tk.Button(master=self.root , text="Search" , font=("Arial" , 18) , background="Blue" , foreground="white" , command=self.search).pack()
        self.weather_statue = "Cloudy"
        self.root.mainloop()
    
        
    def get_weather_info(self):
        try:
            URL = 'http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid=bb681d7c4feaad84e993fba80a2650e9'.format(self.city_name.get().capitalize())
            first_response = requests.get(URL).json()
            self.city = first_response[0]["name"]
            try:
                self.state = first_response[0]["state"]
            except:
                self.state = None
            self.country = first_response[0]["country"]
            self.lat = first_response[0]['lat']
            self.lon = first_response[0]['lon'] 

            URI = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=bb681d7c4feaad84e993fba80a2650e9".format(self.lat , self.lon)
            second_response = requests.get(URI).json()
            self.weather_statue = second_response["weather"][0]["main"]
            self.weather_description = second_response["weather"][0]["description"]
            self.temp_kelvin = second_response["main"]['temp']
            self.temp_celcus = '{:.2f}'.format(self.temp_kelvin - 273,15) 
            self.pressure = second_response["main"]['pressure']
            self.humidity = second_response["main"]['humidity']
        except:
            if messagebox.showerror("Error" , "City Not Founded"):
                self.root.destroy()
                exit()


    def search(self):
        """
        In this method we will update the background of the window depands on the weather 
        creating labels for showing infos about the city (temp , time , weather ...)
        """
        self.display_info()

    def display_info(self):
        self.get_weather_info()
        self.root = tk.Toplevel()
        self.root.title("Weather")
        self.root.iconbitmap(r"C:\Users\DELL\Downloads\Wineass-Ios7-Redesign-Weather.ico")
        self.root.state("zoomed")
        if self.weather_statue == "Clouds":
            self.img = ImageTk.PhotoImage(Image.open(r"C:\Users\DELL\Desktop\Projects_on_Github\Weather_app\cloudy.png"))
            self.img_open = tk.Label(self.root, image = self.img) # adding the image of the company ussing pillow and tkinter(in label we can add text or image)
            self.img_open.place(x = 0 , y=0)
            self.label = tk.Label(self.root , text="About:" , font=("Bold" , 20) , foreground="Purple" , background="White").pack()
            self.label1 = tk.Label(self.root , text=f'City : {self.city} ; State : {self.state} ; Country : {self.country}' , font=("Bold" , 28) , foreground="red" ).pack()
            self.label2 = tk.Label(self.root , text=f'Weather Statue : {self.weather_statue} ; Description : {self.weather_description}' , font=("Bold" , 28) , foreground="Green" ).pack()
            self.label3 = tk.Label(self.root , text=f'Temperature in Kelvin : {self.temp_kelvin} ; Temperature in Celcuis : {self.temp_celcus} ; Pressure : {self.pressure} ; Humidity : {self.humidity}' , font=("Bold" , 20) , foreground="blue" ).pack()
        
        if self.weather_statue == "Clear":
            self.img = ImageTk.PhotoImage(Image.open(r"C:\Users\DELL\Downloads\fluffy-clouds-windy-sky.png"))
            self.img_open = tk.Label(self.root, image = self.img) # adding the image of the company ussing pillow and tkinter(in label we can add text or image)
            self.img_open.place(x = 0 , y=0)
            self.label = tk.Label(self.root , text="About:" , font=("Bold" , 20) , foreground="Purple" , background="White").pack()
            self.label1 = tk.Label(self.root , text=f'City : {self.city} ; State : {self.state} ; Country : {self.country}' , font=("Bold" , 28) , foreground="red" ).pack()
            self.label2 = tk.Label(self.root , text=f'Weather Statue : {self.weather_statue} ; Description : {self.weather_description}' , font=("Bold" , 28) , foreground="Green" ).pack()
            self.label3 = tk.Label(self.root , text=f'Temperature in Kelvin : {self.temp_kelvin} ; Temperature in Celcuis : {self.temp_celcus} ; Pressure : {self.pressure} ; Humidity : {self.humidity}' , font=("Bold" , 20) , foreground="blue" ).pack()
        self.root.mainloop()
        
UI()