import tkinter as tk                 # Import tkinter for GUI
import mysql.connector               # Import MySQL connector for database operations

# ===========================================================
#            CRICKET PLAYER ANALYSIS SYSTEM
# ===========================================================
# This program allows the user to:
# 1. Enter player details.
# 2. Store data in a MySQL database.
# 3. Calculate and display the strike rate of each player.
# ===========================================================


# ===========================================================
#            CONNECT TO MYSQL DATABASE
# ===========================================================
# Connect Python to the MySQL database.
# Make sure the MySQL service is running in XAMPP.

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mcapy"
)

# Create a cursor object for executing SQL queries.

cursor = db.cursor()


# ===========================================================
#               CREATE TABLE
# ===========================================================
# Create the players table if it does not already exist.

cursor.execute("""
CREATE TABLE IF NOT EXISTS players
(
    name VARCHAR(50),
    runs INT,
    balls INT
)
""")


# ===========================================================
#               SAVE PLAYER DATA
# ===========================================================
# Reads data from the Entry boxes and stores it
# in the MySQL database.

def save():

    # Read values entered by the user.
    name = e1.get()
    runs = int(e2.get())
    balls = int(e3.get())

    # SQL INSERT query.
    sql = "INSERT INTO players (name, runs, balls) VALUES (%s, %s, %s)"

    # Store values in a tuple.
    val = (name, runs, balls)

    # Execute the query.
    cursor.execute(sql, val)

    # Save the changes permanently.
    db.commit()

    print("Data Saved!")


# ===========================================================
#            CALCULATE STRIKE RATE
# ===========================================================
# Strike Rate Formula:
#
# Strike Rate = (Runs / Balls) × 100
#
# Fetch all player records and calculate
# the strike rate of each player.

def analyze():

    cursor.execute("SELECT name, runs, balls FROM players")

    rows = cursor.fetchall()

    print("\n------ Strike Rates ------")

    for row in rows:

        name = row[0]
        runs = row[1]
        balls = row[2]

        # Calculate strike rate.
        sr = (runs / balls) * 100

        print(f"{name}: {sr}")


# ===========================================================
#               CREATE GUI WINDOW
# ===========================================================

root = tk.Tk()

# Set the window title.
root.title("Cricket Player Analysis")


# ===========================================================
#               PLAYER NAME
# ===========================================================

tk.Label(root, text="Player Name").pack()

e1 = tk.Entry(root)
e1.pack()


# ===========================================================
#               RUNS
# ===========================================================

tk.Label(root, text="Runs").pack()

e2 = tk.Entry(root)
e2.pack()


# ===========================================================
#               BALLS FACED
# ===========================================================

tk.Label(root, text="Balls").pack()

e3 = tk.Entry(root)
e3.pack()


# ===========================================================
#               BUTTONS
# ===========================================================
# Save Data -> Stores player details.
# Show Analysis -> Calculates strike rate.

tk.Button(root, text="Save Data", command=save).pack()

tk.Button(root, text="Show Analysis", command=analyze).pack()


# ===========================================================
#               START THE APPLICATION
# ===========================================================
# Keeps the GUI running until the user closes it.

root.mainloop()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ mysql.connector.connect()
#    Connects Python with the MySQL database.
#
# ✔ cursor()
#    Creates a cursor object for executing SQL queries.
#
# ✔ execute()
#    Executes SQL commands.
#
# ✔ commit()
#    Saves database changes permanently.
#
# ✔ fetchall()
#    Retrieves all records returned by SELECT.
#
# ✔ INSERT
#    Adds a new record to the table.
#
# ✔ SELECT
#    Retrieves data from the table.
#
# ✔ Tk()
#    Creates the main GUI window.
#
# ✔ Label()
#    Displays text.
#
# ✔ Entry()
#    Accepts user input.
#
# ✔ Button()
#    Creates a clickable button.
#
# ✔ get()
#    Reads data from an Entry widget.
#
# ✔ mainloop()
#    Starts the GUI event loop.
#
# Strike Rate Formula:
# (Runs / Balls) × 100
#
# Example:
# Runs = 75
# Balls = 50
# Strike Rate = (75 / 50) × 100 = 150
# ===========================================================
