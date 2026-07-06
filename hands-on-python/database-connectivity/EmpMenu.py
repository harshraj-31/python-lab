import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="mcapy"
)

curr = mydb.cursor()
#create a table
curr.execute("CREATE TABLE IF NOT EXISTS Emp(eid INT PRIMARY KEY, ename VARCHAR(20),ecity VARCHAR(30) ,esal FLOAT)")


def add():
    eid = int(input("ENTER THE EMPLOYEE ID : "))
    ename = input("Enter the Employee name: ")
    ecity = input("Enter the Employee city: ")
    esal = float(input("Enter the Employee salary: "))

    iq = "INSERT INTO Emp VALUES(%s,%s,%s,%s)"
    val = (eid, ename, ecity, esal)
    curr.execute(iq, val)
    mydb.commit()


#display all students
def display():
    curr.execute("SELECT * FROM Emp")
    rows = curr.fetchall()
    for row in rows:
        print(row)


#Search
def search():
    eid = int(input("Enter the Employee ID to search: "))
    sq = "select * from Emp where eid = %s"
    curr.execute(sq, (eid,))
    row = curr.fetchall()
    if row:
        print(row)
    else:
        print("Employee Not Found")


def update():
    eid = int(input("Enter the employee id: "))
    esal = float(input(f"Enter the updated salary for {eid}: "))

    uq = "UPDATE Emp SET esal = %s WHERE eid = %s"
    val = (esal, eid)
    curr.execute(uq, val)
    mydb.commit()
    print("ROW UPDATED!")


def delete():
    eid = int(input("Enter the employee id: "))
    dq = "DELETE FROM Emp WHERE eid = %s"
    curr.execute(dq, (eid,))
    mydb.commit()
    print(f"{eid} Deleted Successfully")


def total():
    curr.execute("SELECT COUNT(*) FROM Emp")
    tot = curr.fetchone()
    print("Total Employess: ", tot[0])


def distopsal():
    curr.execute("SELECT MAX(esal) FROM Emp")
    topsal = curr.fetchone()
    print("Top Salary: ", topsal[0])


def sortemp():
    sv = input("Enter the column name to sort by (ename,esal,ecity): ")
    if sv == "ename":
        curr.execute(f"SELECT * FROM Emp ORDER BY ename ASC ")
    elif sv == "esal":
        curr.execute(f"SELECT * FROM Emp ORDER BY esal ASC ")
    elif sv == "ecity":
        curr.execute(f"SELECT * FROM Emp ORDER BY ecity ASC ")

    sortemp = curr.fetchall()
    for row in sortemp:
        print(row)


def datainfile():
    yn = input("Are you sure you want to write emp data in a file: ").lower()
    if yn == "n":
        print("Okay , we'll not write data in file")
    elif yn == "y":
        with open("Emp.txt",'w') as f:
            curr.execute("SELECT * FROM Emp")
            for row in curr.fetchall():
                f.write(str(row)+"\n")

        print("Data got written!")
        
    else:
        print("Invalid choice!")


while (True):
    print("----EMPLOYEE'S MANAGEMENT SYSTEM----")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. COUNT TOTAL EMPLOYEE")
    print("7. Display top Salary")
    print("8. Sort")
    print("0. EXIT")

    ch = int(input("ENTER YOUR CHOICE: "))
    match ch:
        case 1:
            add()
        case 2:
            display()
        case 3:
            search()
        case 4:
            update()
        case 5:
            delete()
        case 6:
            total()
        case 7:
            distopsal()

        case 8:
            sortemp()

        case 9:
            datainfile()

        case 0:
            print("Exitinggg")
            break