import mysql.connector
#importing external database sql using sql.connector

#db_name = 'mcapy'

#Connect to MySQL
mydb = mysql.connector.connect(
    host ="localhost",
    port =3306,
    user ="root",
    password ="",
    database ="mcapy"
)

#Create a cursor
curr = mydb.cursor()

#create a table
curr.execute("CREATE TABLE IF NOT EXISTS students(roll_no INT PRIMARY KEY, name VARCHAR(20), marks FLOAT,grade VARCHAR(1))")

def add():
    grade = ''
    sroll = int(input("Enter the student roll no: "))
    sname = input("Enter the Student Name: ")
    marks = float(input("Enter the student's Marks: "))
    if marks >= 75:
        grade = 'A'
    elif marks >= 60 and marks <= 74:
        grade = 'B'
    elif marks >= 50 and marks <= 59:
        grade = 'C'
    elif marks < 50:
        grade = 'F'
    else:
        print("Invalid Marks")

    iq = "insert into students values(%s,%s,%s,%s)"
    val = (sroll,sname,marks,grade)
    curr.execute(iq, val)
    mydb.commit()


#display all students
def display():
    curr.execute("select * from students")
    rows = curr.fetchall()
    for row in rows:
        print(row)


def search():
    srno = int(input("Enter the student's roll no to search: "))
    sq = "select * from students where roll_no = %s"
    curr.execute(sq, (srno,))
    row = curr.fetchall()
    if row:
        print(row)
    else:
        print("Student not found")

def update():
    grade = ''
    srollno= int(input("Enter the student roll no: "))
    marks = float(input("Enter the student's Marks: "))
    if marks >= 75:
        grade = 'A'
    elif marks >= 60 and marks <= 74:
        grade = 'B'
    elif marks >= 50 and marks <= 59:
        grade = 'C'
    elif marks < 50:
        grade = 'F'
    else:
        print("Invalid Marks")

    uq = "update students set marks = %s, grade = %s where roll_no = %s"
    val = (marks,grade,srollno)
    curr.execute(uq,val)
    mydb.commit()

def delete():
    sr = int(input("Enter the student roll no: "))
    dq = "delete from students where roll_no = %s"
    curr.execute(dq,(sr,))
    print(f"{sr} Deleted Successfully")
    mydb.commit()

def distop():
    curr.execute("SELECT MAX(marks) FROM students")
    top = curr.fetchone()
    print("Topper: ",top[0])

def sortstudents():
    sv = input("Enter the choice you want to sort the table (name/marks): ")
    if sv == "name":
        curr.execute("SELECT * FROM students ORDER BY name ASC")
    elif sv == "marks":
        curr.execute("SELECT * FROM students ORDER BY marks ASC")
        
    else:
        print("INVALID CHOICE FOR SORT")
    
    sortstu = curr.fetchall()
    for row in  sortstu:
        print(row)
        
def writeinfile():
    with open("students.txt",'w') as f:
        curr.execute("SELECT * FROM students")
        for row in  curr.fetchall():
            f.write(str(row)+"\n")
        
    print("Data written")

def total():
    curr.execute("SELECT COUNT(*) FROM students")
    tot = curr.fetchone()
    print("Total students: ", tot[0])

while(True):
    print("----STUDENT'S MANAGEMENT SYSTEM----")
    print("1.ADD STUDENT")
    print("2.VIEW ALL STUDENTS")
    print("3.SEARCH STUDENT BY ROLL NO")
    print("4.UPDATE STUDENT DETAILS")
    print("5.DELETE STUDENT")
    print("6.DISPLAY TOPPER")
    print("7.COUNT TOTAL STUDENTS")
    print("8.Sort the table")
    print("9.Write in file")
    print("0.EXIT")
    
    ch = int(input("Enter your choice: "))

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
            distop()

        case 7:
            total()

        case 8:
            sortstudents()
            
        case 9:
            writeinfile()
            
        case 0:
            print("Exitingg")
            break
