import tkinter as tk                 # Import tkinter for GUI
import mysql.connector               # Import MySQL connector to connect Python with MySQL database

# ===========================================================
#            STUDENT MANAGEMENT SYSTEM
# ===========================================================
# This program allows the user to:
# 1. Add student records.
# 2. Store records in a MySQL database.
# 3. Display all student records.
# 4. Clear the input fields.
# ===========================================================


# ===========================================================
#               CONNECT TO MYSQL DATABASE
# ===========================================================
# Establish a connection between Python and MySQL.

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="mcapy"
)

# Create a cursor object.
# Cursor is used to execute SQL queries.

cursor = conn.cursor()


# ===========================================================
#               CREATE TABLE
# ===========================================================
# Creates the table only if it does not already exist.

cursor.execute("""
CREATE TABLE IF NOT EXISTS student
(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
)
""")


# ===========================================================
#               ADD STUDENT
# ===========================================================
# Reads data from the Entry boxes and inserts it
# into the database.

def add_student():

    # Get data entered by the user.
    sid = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    # Check if any field is empty.
    if sid == "" or name == "" or age == "" or course == "":
        status_label.config(text="Fill all fields")
        return

    try:
        # SQL query with placeholders (%s)
        query = "INSERT INTO student VALUES (%s, %s, %s, %s)"

        # Execute the query.
        cursor.execute(query, (int(sid), name, int(age), course))

        # Save the changes permanently.
        conn.commit()

        status_label.config(text="Student Added")

        # Clear all input fields.
        clear_fields()

    except:
        # Display an error if ID already exists.
        status_label.config(text="ID already exists!")


# ===========================================================
#               SHOW ALL STUDENTS
# ===========================================================
# Retrieves all student records from the database
# and displays them in the text area.

def show_students():

    # Remove previous data from the text area.
    text_area.delete("1.0", tk.END)

    # Fetch all records.
    cursor.execute("SELECT * FROM student")

    rows = cursor.fetchall()

    # Display every record.
    for row in rows:

        text_area.insert(
            tk.END,
            "ID: " + str(row[0]) +
            " | Name: " + row[1] +
            " | Age: " + str(row[2]) +
            " | Course: " + row[3] + "\n"
        )


# ===========================================================
#               CLEAR INPUT FIELDS
# ===========================================================
# Removes all text from the Entry widgets.

def clear_fields():

    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)

    status_label.config(text="Fields Cleared")


# ===========================================================
#               CREATE GUI WINDOW
# ===========================================================

root = tk.Tk()

# Set the window title.
root.title("Student System")

# Set the window size.
root.geometry("400x450")


# ===========================================================
#               LABELS AND ENTRY BOXES
# ===========================================================

label_id = tk.Label(root, text="ID")
label_id.pack()

entry_id = tk.Entry(root)
entry_id.pack()


label_name = tk.Label(root, text="Name")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()


label_age = tk.Label(root, text="Age")
label_age.pack()

entry_age = tk.Entry(root)
entry_age.pack()


label_course = tk.Label(root, text="Course")
label_course.pack()

entry_course = tk.Entry(root)
entry_course.pack()


# ===========================================================
#               BUTTONS
# ===========================================================
# Each button is connected to a function.

btn_add = tk.Button(root, text="Add", command=add_student)
btn_add.pack(pady=5)

btn_show = tk.Button(root, text="Show", command=show_students)
btn_show.pack(pady=5)

btn_clear = tk.Button(root, text="Clear", command=clear_fields)
btn_clear.pack(pady=5)


# ===========================================================
#               TEXT AREA
# ===========================================================
# Displays all student records.

text_area = tk.Text(root, height=12)
text_area.pack()


# ===========================================================
#               STATUS LABEL
# ===========================================================
# Displays messages such as:
# Student Added, Fields Cleared, Error, etc.

status_label = tk.Label(root, text="")
status_label.pack()


# ===========================================================
#               START THE APPLICATION
# ===========================================================
# Keeps the GUI running until the user closes it.

root.mainloop()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ mysql.connector.connect()
#    Connects Python to the MySQL database.
#
# ✔ conn.cursor()
#    Creates a cursor object used to execute SQL queries.
#
# ✔ cursor.execute()
#    Executes SQL commands such as CREATE, INSERT, SELECT.
#
# ✔ conn.commit()
#    Saves changes permanently to the database.
#
# ✔ fetchall()
#    Retrieves all rows returned by a SELECT query.
#
# ✔ Tk()
#    Creates the main application window.
#
# ✔ Label()
#    Displays text.
#
# ✔ Entry()
#    Takes user input.
#
# ✔ Button()
#    Creates clickable buttons.
#
# ✔ Text()
#    Displays multiple lines of text.
#
# ✔ get()
#    Reads data from an Entry widget.
#
# ✔ delete()
#    Removes text from Entry or Text widgets.
#
# ✔ insert()
#    Inserts text into a Text widget.
#
# ✔ config()
#    Changes widget properties such as text.
#
# ✔ mainloop()
#    Starts the GUI event loop.
#
# Database Operations Used:
# • CREATE TABLE
# • INSERT
# • SELECT
# ===========================================================
