import tkinter as tk   # Import tkinter library for creating GUI applications

# ===========================================================
#           SHORT NAME GENERATOR USING TKINTER
# ===========================================================
# This program:
# 1. Takes First Name, Middle Name, and Last Name.
# 2. Displays the initials (short name).
#
# Example:
# First Name  : Harshraj
# Middle Name : Mahendrasinh
# Last Name   : Zala
#
# Output:
# H.M.Z
# ===========================================================


# ===========================================================
# CREATE THE MAIN WINDOW
# ===========================================================

m = tk.Tk()


# ===========================================================
# SUBMIT FUNCTION
# ===========================================================
# Reads the names entered by the user
# and displays only the first letter of each name.

def submit():

    # Get text entered in the Entry boxes.
    a = textbox1.get()
    b = textbox2.get()
    c = textbox3.get()

    # Display the initials.
    answer.config(text=f"{a[0]}.{b[0]}.{c[0]}")

    # Another way:
    # answer.config(text=str(a[0]) + "." + str(b[0]) + "." + str(c[0]))


# ===========================================================
# WINDOW SETTINGS
# ===========================================================

# Set the window size.
m.geometry("500x500")

# Set the window title.
m.title("Name")


# ===========================================================
# FIRST NAME
# ===========================================================

# Label
fname = tk.Label(
    m,
    text="Enter First Name :",
    bg="black",
    fg="white"
)

fname.grid(row=0, column=0, padx=10, pady=5)

# Entry box
textbox1 = tk.Entry(m)
textbox1.grid(row=0, column=1, padx=10, pady=5)


# ===========================================================
# MIDDLE NAME
# ===========================================================

mname = tk.Label(
    m,
    text="Enter Middle Name :",
    bg="black",
    fg="white"
)

mname.grid(row=1, column=0, padx=10, pady=5)

textbox2 = tk.Entry(m)
textbox2.grid(row=1, column=1, padx=10, pady=5)


# ===========================================================
# LAST NAME
# ===========================================================

lastname = tk.Label(
    m,
    text="Enter Last Name :",
    bg="black",
    fg="white"
)

lastname.grid(row=2, column=0, padx=10, pady=5)

textbox3 = tk.Entry(m)
textbox3.grid(row=2, column=1, padx=10, pady=5)


# ===========================================================
# SHORT NAME OUTPUT
# ===========================================================

shortname = tk.Label(
    m,
    text="Short Name :",
    bg="black",
    fg="white"
)

shortname.grid(row=3, column=0, padx=10, pady=5)


# ===========================================================
# RESULT LABEL
# ===========================================================
# Displays the generated initials.

answer = tk.Label(
    m,
    text="",
    bg="black",
    fg="yellow",
    width=17
)

answer.grid(row=3, column=1, padx=10, pady=5)


# ===========================================================
# SUBMIT BUTTON
# ===========================================================
# Calls the submit() function when clicked.

sbtn = tk.Button(
    m,
    text="Submit",
    command=submit
)

sbtn.grid(row=4, column=1, padx=10, pady=5)


# ===========================================================
# START THE APPLICATION
# ===========================================================
# Keeps the GUI window running.

m.mainloop()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Tk()
#    Creates the main GUI window.
#
# ✔ Label()
#    Displays text on the window.
#
# ✔ Entry()
#    Takes user input.
#
# ✔ Button()
#    Creates a clickable button.
#
# ✔ grid()
#    Arranges widgets in rows and columns.
#
# ✔ get()
#    Reads text from an Entry widget.
#
# ✔ config()
#    Changes widget properties such as text.
#
# ✔ a[0]
#    Returns the first character of the string.
#
# ✔ f"{a[0]}.{b[0]}.{c[0]}"
#    Uses an f-string to display the initials.
#
# ✔ mainloop()
#    Starts the GUI event loop and keeps the
#    application running.
#
# Example:
# First Name  : Harshraj
# Middle Name : Mahendrasinh
# Last Name   : Zala
#
# Output:
# H.M.Z
# ===========================================================
