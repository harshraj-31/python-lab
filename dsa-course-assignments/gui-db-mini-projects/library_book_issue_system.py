# SET-4: Library Book Issue System

import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


# ---------------- DATABASE CREATION ----------------

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="mcapy"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
cursor.execute("USE library_db")


# ---------------- TABLE CREATION ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS issues (
    student_id INT,
    student_name VARCHAR(50),
    book_title VARCHAR(100),
    genre VARCHAR(50),
    days_issued INT
)
""")

conn.commit()


# ---------------- SAVE RECORD ----------------

def save_record():

    sid = entry_sid.get()
    name = entry_name.get()
    book = entry_book.get()
    genre = entry_genre.get()
    days = entry_days.get()

    try:

        sql = """
        INSERT INTO issues
        (student_id, student_name, book_title, genre, days_issued)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (sid, name, book, genre, days)

        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo(
            "Success",
            "Record Saved"
        )

    except:

        messagebox.showerror(
            "Error",
            "Invalid input"
        )


# ---------------- LOAD DATAFRAME ----------------

def load_dataframe():

    df = pd.read_sql(
        "SELECT * FROM issues",
        conn
    )

    print("\nAll Issue Records:")
    print(df)

    return df


# ---------------- DISPLAY FUNCTIONS ----------------

def most_issued_books():

    df = load_dataframe()

    top = df["book_title"].value_counts().head()

    print("\nMost issued books (top records):")
    print(top)


def students_more_than_10_days():

    df = load_dataframe()

    result = df[df["days_issued"] > 10]

    print("\nStudents who issued books for more than 10 days:")
    print(result[["student_name", "book_title", "days_issued"]])


# ---------------- PLOTS ----------------

def plot_bar():

    df = load_dataframe()

    counts = df["genre"].value_counts()

    counts.plot(kind="bar")

    plt.title("Number of Books Issued per Genre")

    plt.xlabel("Genre")
    plt.ylabel("Number of Books")

    plt.show()


def plot_pie():

    df = load_dataframe()

    counts = df["genre"].value_counts()

    counts.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Genre Distribution")

    plt.ylabel("")

    plt.show()


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Library Book Issue System")

tk.Label(root, text="Student ID").grid(row=0, column=0)
entry_sid = tk.Entry(root)
entry_sid.grid(row=0, column=1)

tk.Label(root, text="Student Name").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Book Title").grid(row=2, column=0)
entry_book = tk.Entry(root)
entry_book.grid(row=2, column=1)

tk.Label(root, text="Genre").grid(row=3, column=0)
entry_genre = tk.Entry(root)
entry_genre.grid(row=3, column=1)

tk.Label(root, text="Days Issued").grid(row=4, column=0)
entry_days = tk.Entry(root)
entry_days.grid(row=4, column=1)


tk.Button(
    root,
    text="Save Record",
    command=save_record
).grid(row=5, column=0)

tk.Button(
    root,
    text="Most Issued Books",
    command=most_issued_books
).grid(row=5, column=1)

tk.Button(
    root,
    text="Issued > 10 Days",
    command=students_more_than_10_days
).grid(row=6, column=0)

tk.Button(
    root,
    text="Bar Chart (Genre)",
    command=plot_bar
).grid(row=6, column=1)

tk.Button(
    root,
    text="Pie Chart (Genre)",
    command=plot_pie
).grid(row=7, column=0)


root.mainloop()

conn.close()