# SET-6: Hospital Billing Analytics System

import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


# ---------------- DATABASE CONNECTION ----------------

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="mcapy"
)

cursor = conn.cursor()


# ---------------- CREATE TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS hospital (
    hospital_id INT,
    patient_name VARCHAR(50),
    disease VARCHAR(50),
    age INT,
    bill FLOAT
)
""")

conn.commit()


# ---------------- SAVE RECORD ----------------

def save_record():

    hid = entry_id.get()
    name = entry_name.get()
    disease = entry_disease.get()
    age = entry_age.get()
    bill = entry_bill.get()

    try:

        sql = """
        INSERT INTO hospital
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (hid, name, disease, age, bill)

        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo(
            "Success",
            "Record Saved"
        )

    except:

        messagebox.showerror(
            "Error",
            "Invalid input or duplicate ID"
        )


# ---------------- LOAD DATAFRAME ----------------

def load_dataframe():

    df = pd.read_sql_query(
        "SELECT * FROM hospital",
        conn
    )

    print("\nAll Records:")
    print(df)

    return df


# ---------------- DISPLAY FUNCTIONS ----------------

def total_billing():

    df = load_dataframe()

    result = df.groupby("disease")["bill"].sum()

    print("\nTotal billing per disease:")
    print(result)


def patients_above_60():

    df = load_dataframe()

    result = df[df["age"] > 60]

    print("\nPatients above age 60:")
    print(result)


def sort_by_bill():

    df = load_dataframe()

    result = df.sort_values(
        by="bill",
        ascending=False
    )

    print("\nPatients sorted by bill amount (descending):")
    print(result)


# ---------------- PLOTS ----------------

def plot_bar():

    df = load_dataframe()

    result = df.groupby("disease")["bill"].sum()

    result.plot(kind="bar")

    plt.title("Total Billing per Disease")

    plt.xlabel("Disease")
    plt.ylabel("Total Bill")

    plt.show()


def plot_histogram():

    df = load_dataframe()

    plt.hist(df["age"])

    plt.title("Histogram of Patient Ages")

    plt.xlabel("Age")
    plt.ylabel("Frequency")

    plt.show()


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Hospital Billing System")

tk.Label(root, text="Hospital ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Patient Name").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Disease").grid(row=2, column=0)
entry_disease = tk.Entry(root)
entry_disease.grid(row=2, column=1)

tk.Label(root, text="Age").grid(row=3, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1)

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
    command=total_billing
).grid(row=5, column=1)

tk.Button(
    root,
    text="Patients Above 60",
    command=patients_above_60
).grid(row=6, column=0)

tk.Button(
    root,
    text="Sort by Bill",
    command=sort_by_bill
).grid(row=6, column=1)

tk.Button(
    root,
    text="Bar Chart",
    command=plot_bar
).grid(row=7, column=0)

tk.Button(
    root,
    text="Histogram",
    command=plot_histogram
).grid(row=7, column=1)


root.mainloop()

conn.close()