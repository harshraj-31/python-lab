# Import MySQL connector module
import mysql.connector as conn

# Establish connection with MySQL database
mydb = conn.connect(
    host="localhost",      # Server name (localhost = your computer)
    user="root",           # MySQL username
    password="",           # MySQL password
    database="mcapy"       # Database you want to use
)

# Create cursor object (used to execute SQL queries)
cursor = mydb.cursor()

# Create table 'Emp' if it does not already exist
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Emp(Eid INT PRIMARY KEY, Ename VARCHAR(20), EDOB VARCHAR(20))"
)

print("Table Created")

# Insert a record into Emp table
eiq = "INSERT INTO Emp VALUES(%s,%s,%s)"   # SQL insert query
val = (1, 'Arnold', '12-6-2003')           # Values to insert

cursor.execute(eiq, val)   # Execute insert query

# Save changes permanently in database
mydb.commit()


# Fetch all records from Emp table
cursor.execute("SELECT * FROM Emp")

# Display records one by one
for row in cursor:
    print(row)