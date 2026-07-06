# SET-2: Cricket Player Statistics System

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

cursor.execute("CREATE DATABASE IF NOT EXISTS cricket_db")

cursor.execute("USE cricket_db")


# ---------------- TABLE CREATION ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    team VARCHAR(50),
    match_id INT,
    runs INT,
    balls INT,
    wickets INT
)
""")

conn.commit()


# ---------------- SAVE RECORD ----------------

def save_record():

    name = entry_name.get()
    team = entry_team.get()
    match_id = entry_match.get()
    runs = entry_runs.get()
    balls = entry_balls.get()
    wickets = entry_wickets.get()

    try:

        sql = """
        INSERT INTO players
        (name, team, match_id, runs, balls, wickets)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            name,
            team,
            match_id,
            runs,
            balls,
            wickets
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
            "Invalid data"
        )


# ---------------- LOAD DATAFRAME ----------------

def load_dataframe():

    df = pd.read_sql(
        "SELECT * FROM players",
        conn
    )

    print("\nAll Player Records:")
    print(df)

    return df


# ---------------- DISPLAY ----------------

def strike_rate():

    df = load_dataframe()

    df["StrikeRate"] = (
        df["runs"] / df["balls"]
    ) * 100

    print("\nStrike Rate of each player:")
    print(df[["name", "StrikeRate"]])


def top_players():

    df = load_dataframe()

    top = df.sort_values(
        by="runs",
        ascending=False
    ).head(5)

    print("\nTop 5 players based on runs:")
    print(top[["name", "runs"]])


# ---------------- PLOTS ----------------

def plot_bar():

    df = load_dataframe()

    totals = df.groupby("name")["runs"].sum()

    totals.plot(kind="bar")

    plt.title("Total Runs by Player")

    plt.xlabel("Player")

    plt.ylabel("Runs")

    plt.show()


def plot_line():

    df = load_dataframe()

    wickets = df.groupby("name")["wickets"].sum()

    plt.plot(wickets.index, wickets.values)

    plt.title("Wickets Taken by Player")

    plt.xlabel("Player")

    plt.ylabel("Wickets")

    plt.show()


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Cricket Player Statistics")

tk.Label(root, text="Player Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Team").grid(row=1, column=0)
entry_team = tk.Entry(root)
entry_team.grid(row=1, column=1)

tk.Label(root, text="Match ID").grid(row=2, column=0)
entry_match = tk.Entry(root)
entry_match.grid(row=2, column=1)

tk.Label(root, text="Runs Scored").grid(row=3, column=0)
entry_runs = tk.Entry(root)
entry_runs.grid(row=3, column=1)

tk.Label(root, text="Balls Faced").grid(row=4, column=0)
entry_balls = tk.Entry(root)
entry_balls.grid(row=4, column=1)

tk.Label(root, text="Wickets Taken").grid(row=5, column=0)
entry_wickets = tk.Entry(root)
entry_wickets.grid(row=5, column=1)


tk.Button(
    root,
    text="Save Record",
    command=save_record
).grid(row=6, column=0)

tk.Button(
    root,
    text="Strike Rate",
    command=strike_rate
).grid(row=6, column=1)

tk.Button(
    root,
    text="Top 5 Players",
    command=top_players
).grid(row=7, column=0)

tk.Button(
    root,
    text="Bar Chart (Runs)",
    command=plot_bar
).grid(row=7, column=1)

tk.Button(
    root,
    text="Line Graph (Wickets)",
    command=plot_line
).grid(row=8, column=0)


root.mainloop()

conn.close()