import tkinter as tk


# 1. Create the main window
main = tk.Tk()
main.title("Friendly GUI")
main.geometry("600x600")

# 2. Create a widget
label = tk.Label(main,text="Stillness is the Key",bg="Grey",fg="black")

# 3. Position the widget

#i.  pack()
#ii. place()
#iii. grid()

label.place(x = 250, y=250) #x = horizontal, y = vertical

#4. Run the application
main.mainloop()