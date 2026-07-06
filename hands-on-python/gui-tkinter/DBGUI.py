import tkinter as tk
import mysql.connector

# ---------------- DATABASE SETUP ----------------
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="mcapy"
)

cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS student (id INT PRIMARY KEY,name VARCHAR(50), age INT, course VARCHAR(50))")

# ---------------- FUNCTIONS ----------------
def add_student():
    sid = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    if sid == "" or name == "" or age == "" or course == "":
        status_label.config(text="Fill all fields")
        return

    try:
        query = "INSERT INTO student VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (int(sid), name, int(age), course))
        conn.commit()
        status_label.config(text="Student Added")
        clear_fields()
    except:
        status_label.config(text="ID already exists!")

def show_students():
    text_area.delete("1.0", tk.END)

    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    for row in rows:
        text_area.insert(tk.END,
            "ID: " + str(row[0]) +
            " | Name: " + row[1] +
            " | Age: " + str(row[2]) +
            " | Course: " + row[3] + "\n"
        )


def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    status_label.config(text="Fields Cleared")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student System")
root.geometry("400x450")


#Labels
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


#Buttons
btn_add = tk.Button(root, text="Add", command=add_student)
btn_add.pack(pady=5)

btn_show = tk.Button(root, text="Show", command=show_students)
btn_show.pack(pady=5)

btn_clear = tk.Button(root, text="Clear", command=clear_fields)
btn_clear.pack(pady=5)


# Text area
text_area = tk.Text(root, height=12)
text_area.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()