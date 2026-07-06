import tkinter as tk
import mysql.connector

# 1. Connect to XAMPP MySQL
# Make sure MySQL is "Running" in your XAMPP Control Panel
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mcapy" 
)
cursor = db.cursor()
cursor .execute("CREATE TABLE IF NOT EXISTS players (name VARCHAR(50),runs INT,balls INT)")

# 2. Function to Save Data
def save():
    # Get values from the entry boxes
    name = e1.get()
    runs = int(e2.get())
    balls = int(e3.get())
    
    # SQL command to insert data
    sql = "INSERT INTO players (name, runs, balls) VALUES (%s, %s, %s)"
    val = (name, runs, balls)
    
    cursor.execute(sql, val)
    db.commit()
    print("Data Saved!")

# 3. Function to Calculate Strike Rate
def analyze():
    cursor.execute("SELECT name, runs, balls FROM players")
    rows = cursor.fetchall()
    
    print("\n--- Strike Rates ---")
    for row in rows:
        name = row[0]
        runs = row[1]
        balls = row[2]
        # Calculation: (Runs / Balls) * 100
        sr = (runs / balls) * 100
        print(f"{name}: {sr}")

# 4. Simple GUI Window
root = tk.Tk()

tk.Label(root, text="Player Name").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Runs").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Balls").pack()
e3 = tk.Entry(root)
e3.pack()

tk.Button(root, text="Save Data", command=save).pack()
tk.Button(root, text="Show Analysis", command=analyze).pack()

root.mainloop()