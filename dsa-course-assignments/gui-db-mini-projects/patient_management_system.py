# Patient Management System
# MySQL database created from Python

import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


# ---------------- CREATE DATABASE ----------------

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="mcapy"
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_db")

cursor.execute("USE hospital_db")


# ---------------- CREATE TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    disease VARCHAR(50),
    bill FLOAT
)
""")

conn.commit()


# ---------------- SAVE RECORD ----------------

def save_record():

    pid = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    disease = entry_disease.get()
    bill = entry_bill.get()

    try:

        sql = """
        INSERT INTO patients
        (id, name, age, disease, bill)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (pid, name, age, disease, bill)

        cursor.execute(sql, values)

        conn.commit()

        messagebox.showinfo("Success", "Record Saved")

    except:

        messagebox.showerror(
            "Error",
            "ID already exists or invalid input"
        )


# ---------------- LOAD DATAFRAME ----------------

def load_dataframe():

    df = pd.read_sql(
        "SELECT * FROM patients",
        conn
    )

    print("\nAll Records:")
    print(df)

    return df


# ---------------- DISPLAY ----------------

def billing_per_disease():

    df = load_dataframe()

    result = df.groupby("disease")["bill"].sum()

    print("\nTotal billing per disease:")
    print(result)


def patients_above_60():

    df = load_dataframe()

    result = df[df["age"] > 60]

    print("\nPatients above age 60:")
    print(result)


# ---------------- PLOTS ----------------

def plot_bar():

    df = load_dataframe()

    counts = df["disease"].value_counts()

    counts.plot(kind="bar")

    plt.title("Patients per Disease")

    plt.show()


def plot_histogram():

    df = load_dataframe()

    plt.hist(df["age"])

    plt.title("Histogram of Patient Ages")

    plt.show()


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Patient Management System")

tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Age").grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

tk.Label(root, text="Disease").grid(row=3, column=0)
entry_disease = tk.Entry(root)
entry_disease.grid(row=3, column=1)

tk.Label(root, text="Bill Amount").grid(row=4, column=0)
entry_bill = tk.Entry(root)
entry_bill.grid(row=4, column=1)


tk.Button(
    root,
    text="Save Record",
    command=save_record
).grid(row=5, column=0)

tk.Button(
    root,
    text="Total Billing per Disease",
    command=billing_per_disease
).grid(row=5, column=1)

tk.Button(
    root,
    text="Patients Above Age 60",
    command=patients_above_60
).grid(row=6, column=0)

tk.Button(
    root,
    text="Bar Chart",
    command=plot_bar
).grid(row=6, column=1)

tk.Button(
    root,
    text="Histogram",
    command=plot_histogram
).grid(row=7, column=0)


root.mainloop()

conn.close()