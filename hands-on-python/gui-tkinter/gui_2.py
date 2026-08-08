import tkinter as tk   # Import tkinter for creating GUI applications


# ===========================================================
#             STUDENT REGISTRATION FORM
# ===========================================================
# This program creates a student registration form.
#
# It takes:
# - Name
# - Age
# - City
# - Hobbies
# - Gender
#
# After clicking SUBMIT, all entered details are displayed.
# ===========================================================


# ===========================================================
#                    SUBMIT FUNCTION
# ===========================================================
# This function collects all the information entered
# by the user and displays it in the result label.

def submit():

    # Get values from the Entry and Spinbox widgets.
    student_name = nametxt.get()
    age = agetxt.get()
    city = citytxt.get()
    gender = gendertxt.get()

    # Create an empty list to store selected hobbies.
    hobbies = []

    # Check which hobby checkboxes are selected.
    #
    # var.get() returns:
    # 1 -> Checkbox is selected
    # 0 -> Checkbox is not selected

    for var, hobby_name in [
        (gym, "GYM"),
        (music, "MUSIC"),
        (reading, "READING")
    ]:

        if var.get():
            hobbies.append(hobby_name)

    # Display all entered information.
    showinfo.config(
        text="Name: " + student_name +
             " Age: " + age +
             " City: " + city +
             " Hobbies: " + str(hobbies) +
             " Gender: " + gender
    )


# ===========================================================
#              CREATE AND CONFIGURE WINDOW
# ===========================================================

window = tk.Tk()

# Set the size of the window.
window.geometry("600x600")

# Set the title displayed at the top.
window.title("Student Registration Form")

# Set the background color.
window.config(background="grey")


# ===========================================================
#                  NAME FIELD
# ===========================================================

name_label = tk.Label(
    window,
    text="Name",
    bg="black",
    fg="white"
)

name_label.place(x=100, y=70)


# Entry widget is used to take single-line text input.
nametxt = tk.Entry(
    window,
    bg="white",
    fg="black"
)

nametxt.place(x=160, y=70)


# ===========================================================
#                   AGE FIELD
# ===========================================================

age_label = tk.Label(
    window,
    text="Age",
    bg="black",
    fg="white"
)

age_label.place(x=100, y=120)


# -----------------------------------------------------------
#                    SPINBOX
# -----------------------------------------------------------
# Spinbox allows the user to select a value using
# up and down arrows.
#
# It is useful for:
# - Age
# - Quantity
# - Marks
# - Number of items

agetxt = tk.Spinbox(
    window,
    from_=0,
    to=100,
    bg="white",
    fg="black"
)

agetxt.place(x=160, y=120)


# ===========================================================
#                   CITY FIELD
# ===========================================================

city_label = tk.Label(
    window,
    text="City",
    bg="black",
    fg="white"
)

city_label.place(x=100, y=170)


citytxt = tk.Entry(
    window,
    bg="white",
    fg="black"
)

citytxt.place(x=160, y=170)


# ===========================================================
#                  HOBBIES SECTION
# ===========================================================
# Checkbuttons are used because a person can select
# more than one hobby at the same time.

hobby_label = tk.Label(
    window,
    text="Hobbies",
    bg="black",
    fg="white"
)

hobby_label.place(x=100, y=220)


# -----------------------------------------------------------
# VARIABLES FOR CHECKBOXES
# -----------------------------------------------------------
# IntVar() stores the state of a Checkbutton.
#
# 0 -> Not selected
# 1 -> Selected

gym = tk.IntVar()
music = tk.IntVar()
reading = tk.IntVar()


# -----------------------------------------------------------
# HOBBY CHECKBOXES
# -----------------------------------------------------------

tk.Checkbutton(
    window,
    text="GYM",
    variable=gym
).place(x=160, y=220)

tk.Checkbutton(
    window,
    text="MUSIC",
    variable=music
).place(x=220, y=220)

tk.Checkbutton(
    window,
    text="READING",
    variable=reading
).place(x=290, y=220)


# ===========================================================
#                  GENDER SECTION
# ===========================================================
# Radio buttons are used when the user should select
# only ONE option from multiple choices.

gender_label = tk.Label(
    window,
    text="Gender",
    bg="black",
    fg="white"
)

gender_label.place(x=100, y=280)


# -----------------------------------------------------------
# RADIO BUTTON VARIABLE
# -----------------------------------------------------------
# All radio buttons use the same StringVar().
# The selected button's value is stored in this variable.

gendertxt = tk.StringVar()

# Set Male as the default selection.
gendertxt.set("Male")


# -----------------------------------------------------------
# MALE / FEMALE RADIO BUTTONS
# -----------------------------------------------------------

tk.Radiobutton(
    window,
    text="Male",
    variable=gendertxt,
    value="Male",
    fg="black",
    bg="red"
).place(x=160, y=280)


tk.Radiobutton(
    window,
    text="Female",
    variable=gendertxt,
    value="Female",
    fg="black",
    bg="red"
).place(x=220, y=280)


# ===========================================================
#                    SUBMIT BUTTON
# ===========================================================
# When the button is clicked, submit() function is called.

subbtn = tk.Button(
    window,
    text="SUBMIT",
    command=submit,
    fg="black",
    bg="white"
)

subbtn.place(x=180, y=350)


# ===========================================================
#                  RESULT LABEL
# ===========================================================
# This label displays the student's details
# after clicking the Submit button.

showinfo = tk.Label(
    window,
    text="",
    bg="white",
    fg="black"
)

showinfo.place(x=100, y=400)


# ===========================================================
#                 START THE APPLICATION
# ===========================================================
# mainloop() keeps the GUI running and waits
# for user actions such as button clicks.

window.mainloop()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Entry()
#    Takes single-line text input.
#
# ✔ Spinbox()
#    Allows selecting a number using up/down arrows.
#
# ✔ Checkbutton()
#    Allows selecting multiple options.
#
# ✔ IntVar()
#    Stores the selected/unselected state of a Checkbutton.
#
# ✔ Radiobutton()
#    Allows selecting only one option from a group.
#
# ✔ StringVar()
#    Stores the selected value of a Radiobutton.
#
# ✔ get()
#    Retrieves the value from Entry, Spinbox, or variables.
#
# ✔ config()
#    Changes widget properties such as displayed text.
#
# ✔ place()
#    Positions widgets using x and y coordinates.
#
# ✔ command=submit
#    Calls the submit() function when the button is clicked.
#
# ✔ mainloop()
#    Starts the Tkinter event loop.
# ===========================================================
