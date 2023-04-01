from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.title("Time Zones")
root.geometry("800x700")

india = ImageTk.PhotoImage(Image.open("india.jpg"))
usa = ImageTk.PhotoImage(Image.open("usa.jpg"))
australia = ImageTk.PhotoImage(Image.open("australia.jpg"))
japan = ImageTk.PhotoImage(Image.open("japan.jpg"))


label_india = Label(root, text = "India")
label_india.place(relx = 0.25, rely = 0.05, anchor = CENTER)
india_image = Label(root)
india_image["image"] = india
india_image.place(relx = 0.25, rely = 0.25, anchor = CENTER)
india_time = Label(root)
india_time.place(relx = 0.25, rely = 0.32, anchor = CENTER)

label_usa = Label(root, text = "USA")
label_usa.place(relx = 0.75, rely = 0.05, anchor = CENTER)
usa_image = Label(root)
usa_image["image"] = usa
usa_image.place(relx = 0.75, rely = 0.25, anchor = CENTER)
usa_time = Label(root)
usa_time.place(relx = 0.75, rely = 0.32, anchor = CENTER)

label_australia = Label(root, text = "Australia")
label_australia.place(relx = 0.25, rely = 0.48, anchor = CENTER)
australia_image = Label(root)
australia_image["image"] = australia
australia_image.place(relx = 0.25, rely = 0.68, anchor = CENTER)
australia_time = Label(root)
australia_time.place(relx = 0.25, rely = 0.7, anchor = CENTER)

label_japan = Label(root, text = "Japan")
label_japan.place(relx = 0.75, rely = 0.48, anchor = CENTER)
japan_image = Label(root)
japan_image["image"] = japan
japan_image.place(relx = 0.75, rely = 0.68, anchor = CENTER)
japan_time = Label(root)
japan_time.place(relx = 0.75, rely = 0.7, anchor = CENTER)

class India:
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = current_time
        india_time.after(200,self.times)
        
class USA:
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time["text"] = current_time
        usa_time.after(200,self.times)
        
class Australia:
    def times(self):
        home = pytz.timezone("Australia/ACT")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        australia_time["text"] = current_time
        australia_time.after(200,self.times)
        
class Japan:
    def times(self):
        home = pytz.timezone("Japan")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        japan_time["text"] = current_time
        japan_time.after(200,self.times)
        
obj_india = India()
obj_usa = USA()
obj_australia = Australia()
obj_japan = Japan()

btn1 = Button(root, text = "Show Time", command = obj_india.times)        
btn2 = Button(root, text = "Show Time", command = obj_usa.times) 
btn3 = Button(root, text = "Show Time", command = obj_australia.times) 
btn4 = Button(root, text = "Show Time", command = obj_japan.times) 
btn1.place(relx = 0.25, rely = 0.4, anchor = CENTER)
btn2.place(relx = 0.75, rely = 0.4, anchor = CENTER)
btn3.place(relx = 0.25, rely = 0.8, anchor = CENTER)
btn4.place(relx = 0.75, rely = 0.8, anchor = CENTER)

root.mainloop()
