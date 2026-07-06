import tkinter as tk
m = tk.Tk()

def submit():#method for submit
    
    a = textbox1.get()
    b = textbox2.get()
    c = textbox3.get()
    answer.config(text=f"{a[0]}.{b[0]}.{c[0]}")
    # or👇
    # answer.config(text = str(a[0]) + "." + str(b[0]) + "." + str(c))
    
    
m.geometry("500x500")#window geometry

m.title("Name ")#title of the output window

#text output = fname
fname=tk.Label(m,text="Enter First Name :",bg="black",fg="white")
fname.grid(row=0, column=0,padx=10,pady=5)

#input entry 1
textbox1=tk.Entry(m)
textbox1.grid(row=0, column=1,padx=10,pady=5)

#text output = mname
mname=tk.Label(m,text="Enter Middle Name  :",bg="black",fg="white")
mname.grid(row=1, column=0,padx=10,pady=5)

#input entry 2
textbox2=tk.Entry(m)
textbox2.grid(row=1, column=1,padx=10,pady=5)

#text output = lastname
lastname=tk.Label(m,text="Enter Last Name  :",bg="black",fg="white")
lastname.grid(row=2, column=0,padx=10,pady=5)

#input entry 3
textbox3=tk.Entry(m)
textbox3.grid(row=2, column=1,padx=10,pady=5)


#text output = name
shortname=tk.Label(m,text="Short Name :",bg="black",fg="white")
shortname.grid(row=3, column=0,padx=10,pady=5)

#text output = answer
answer=tk.Label(m,text="",bg="black",fg="yellow",width=17)
answer.grid(row=3, column=1,padx=10,pady=5)

#submit button 
sbtn = tk.Button(m, text='Submit', command=submit)
sbtn.grid(row=4, column=1,padx=10,pady=5)
m.mainloop()