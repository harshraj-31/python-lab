import tkinter as tk
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    timelabel.config(text=time_string)

    day_string = strftime("%A")
    daylabel.config(text=day_string)
    
    date_string = strftime("%B %d, %Y")
    datelabel.config(text=date_string)

    timelabel.after(1000,update)


m = tk.Tk()
m.geometry("500x500")
m.title("Clock")
m.config(background="black")


#LABELS
timelabel = tk.Label(m,font=("Arial",50), fg="green")
timelabel.place(x=80, y=100)


daylabel = tk.Label(m,font=("Ink Free",25),fg="red",bg="white")
daylabel.place(x=150,y=210)


datelabel = tk.Label(m,font=("Ink Free",25),fg="blue",bg="white")
datelabel.place(x=100,y=320)

update()

m.mainloop()