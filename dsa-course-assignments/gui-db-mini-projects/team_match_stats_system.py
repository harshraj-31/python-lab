# SET-3: Team Match Statistics System

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

cursor.execute("CREATE DATABASE IF NOT EXISTS match_db")
cursor.execute("USE match_db")


# ---------------- TABLE CREATION ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
    match_id INT PRIMARY KEY,
    team VARCHAR(50),
    runs INT,
    wickets INT,
    overs FLOAT,
    result VARCHAR(10)
)
""")

conn.commit()


# ---------------- SAVE RECORD ----------------

def save_record():

    mid = entry_match.get()
    team = entry_team.get()
    runs = entry_runs.get()
    wickets = entry_wickets.get()
    overs = entry_overs.get()
    result = entry_result.get()

    try:

        sql = """
        INSERT INTO matches
        (match_id, team, runs, wickets, overs, result)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            mid,
            team,
            runs,
            wickets,
            overs,
            result
        )

        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo(
            "Success",
            "Record Saved"
        )

    except:

        messagebox.showerror(
            "Error",
            "Match ID already exists"
        )


# ---------------- LOAD DATAFRAME ----------------

def load_dataframe():

    df = pd.read_sql(
        "SELECT * FROM matches",
        conn
    )

    print("\nAll Match Records:")
    print(df)

    return df


# ---------------- DISPLAY FUNCTIONS ----------------

def average_runs():

    df = load_dataframe()

    avg = df.groupby("team")["runs"].mean()

    print("\nAverage runs scored by each team:")
    print(avg)


def win_percentage():

    df = load_dataframe()

    total_matches = df.groupby("team").size()

    wins = df[df["result"] == "Win"].groupby("team").size()

    percentage = (wins / total_matches) * 100

    print("\nWin percentage of each team:")
    print(percentage)


# ---------------- PLOTS ----------------

def plot_bar():

    df = load_dataframe()

    total_matches = df.groupby("team").size()
    wins = df[df["result"] == "Win"].groupby("team").size()

    percentage = (wins / total_matches) * 100

    percentage.plot(kind="bar")

    plt.title("Win Percentage by Team")
    plt.xlabel("Team")
    plt.ylabel("Win %")

    plt.show()


def plot_histogram():

    df = load_dataframe()

    plt.hist(df["runs"])

    plt.title("Histogram of Runs Scored")
    plt.xlabel("Runs")
    plt.ylabel("Frequency")

    plt.show()


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Team Match Statistics System")

tk.Label(root, text="Match ID").grid(row=0, column=0)
entry_match = tk.Entry(root)
entry_match.grid(row=0, column=1)

tk.Label(root, text="Team Name").grid(row=1, column=0)
entry_team = tk.Entry(root)
entry_team.grid(row=1, column=1)

tk.Label(root, text="Runs Scored").grid(row=2, column=0)
entry_runs = tk.Entry(root)
entry_runs.grid(row=2, column=1)

tk.Label(root, text="Wickets Lost").grid(row=3, column=0)
entry_wickets = tk.Entry(root)
entry_wickets.grid(row=3, column=1)

tk.Label(root, text="Overs Played").grid(row=4, column=0)
entry_overs = tk.Entry(root)
entry_overs.grid(row=4, column=1)

tk.Label(root, text="Result (Win/Loss)").grid(row=5, column=0)
entry_result = tk.Entry(root)
entry_result.grid(row=5, column=1)


tk.Button(
    root,
    text="Save Record",
    command=save_record
).grid(row=6, column=0)

tk.Button(
    root,
    text="Average Runs",
    command=average_runs
).grid(row=6, column=1)

tk.Button(
    root,
    text="Win Percentage",
    command=win_percentage
).grid(row=7, column=0)

tk.Button(
    root,
    text="Bar Chart (Win %)",
    command=plot_bar
).grid(row=7, column=1)

tk.Button(
    root,
    text="Histogram (Runs)",
    command=plot_histogram
).grid(row=8, column=0)


root.mainloop()

conn.close()