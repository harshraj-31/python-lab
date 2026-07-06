import tkinter as tk



def submit():
    name = nametxt.get()
    age = agetxt.get()
    city = citytxt.get()
    gen = gendertxt.get()
    hobbies = []
    for var,name in [(gym,"GYM"),(music,"MUSIC"),(reading,"READING")]:
        if var.get():
            hobbies.append(name)
    
    showinfo.config(text="Name: "+name+" Age: "+age+" City: "+city+" Hobbies: "+str(hobbies)+" Gender: "+gen)



#Window initialise annd settings
window = tk.Tk()
window.geometry("600x600")
window.title("Student Registeration Form")
window.config(background="grey")


#labels & Entryboxes
name = tk.Label(window,text="Name",bg="black",fg="white") #name Label
name.place(x=100,y=70)

nametxt = tk.Entry(window,bg="white",fg="black") #name entry
nametxt.place(x=160,y=70)



age = tk.Label(window,text="Age",bg="black",fg="white") #age Label
age.place(x=100,y=120)

#Spinbox use ↑ ↓ arrows to increase/decrease Best for:
# Age
# Quantity
# Marks

agetxt = tk.Spinbox(window,from_=0 , to=100, bg="white",fg="black") #age entry
agetxt.place(x=160,y=120)


city = tk.Label(window,text="City",bg="black",fg="white") #city Label
city.place(x=100,y=170)


citytxt = tk.Entry(window,bg="white",fg="black") #city entry
citytxt.place(x=160,y=170)


#USING CHECKBOX FOR HOBBIES
hobby = tk.Label(window,text="Hobbies",bg="black",fg="white") #Hobby Label
hobby.place(x=100,y=220)

#hobbiesforCheckBox:
gym=tk.IntVar() # gym variable for check box
music=tk.IntVar()# music variable for check box
reading= tk.IntVar() # reading variable for check box

#CHECBOX - A person can select one OR many
tk.Checkbutton(window,text="GYM",variable=gym).place(x=160,y=220) #Hobbies CheckBoxes
tk.Checkbutton(window,text="MUSIC",variable=music).place(x=220,y=220) #Hobbies CheckBoxes
tk.Checkbutton(window,text="READING",variable=reading).place(x=290,y=220)# Hobbies CheckBoxes



#USING RADIO BUTTON FOR GENDER
gender = tk.Label(window,text="Gender",bg="black",fg="white") #Gender Label
gender.place(x=100,y=280)

#All radio buttons share ONE variable,That variable stores the selected value
gendertxt = tk.StringVar() #Gender variable
gendertxt.set("Male") #default value

#MALE/FEMALE RADIO BUTTONS
tk.Radiobutton(window,text="Male",variable=gendertxt,value="Male",fg="black",bg="red").place(x=160,y=280)
tk.Radiobutton(window,text="Female",variable=gendertxt,value="Female",fg="black",bg="red").place(x=220,y=280)



#SUBMIT BUTTON
subbtn = tk.Button(window,text="SUBMIT",command=submit,fg="Black",bg="White")
subbtn.place(x=180,y=350)

#Label top show details:
showinfo = tk.Label(window,text="",bg="white",fg="black")
showinfo.place(x=100,y=400)


window.mainloop()