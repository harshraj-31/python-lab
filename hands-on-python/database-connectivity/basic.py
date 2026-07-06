# import mysql.connector
# #importing external database sql using sql.connector

# #db_name = 'mcapy'

# #Connect to MySQL
# mydb = mysql.connector.connect(
#     host ="localhost",
#     port =3306,
#     user ="root",
#     password ="",
#     database ="mcapy"
# )

# #Create a cursor
# curr = mydb.cursor()


# #create a table
# curr.execute("CREATE TABLE IF NOT EXISTS (id INT PRIMARY KEY, name VARCHAR(20))")

# #INSERTING VALUES for n students
# n = int(input("How many students data you want to enter: "))
# for i in range(1,n+1):
#     sid = int(input(f"Enter the {i} student's ID: "))
#     sname = input(f"Enter the {i} students name: ")
#     val = (sid,sname)
#     curr.execute("INSERT INTO stud VALUES(%s,%s)",val)
#     print(f"{i}'s data Inserted")


# mydb.commit()

# curr.execute("SELECT * FROM STUD")
# rows = curr.fetchall()


# print("Table Data: ")
# for row in rows:
#     print(row)


#import mysql connector
import mysql.connector as conn


# COnnect with database
mydb = conn.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="mcapy" 
)

#Create a cursor
curr = mydb.cursor()


#creating a table
curr.execute("CREATE TABLE IF NOT EXISTS Product(Pid INT PRIMARY KEY, Pname VARCHAR(30),Pprice FLOAT)")


# n = int(input("How many products you want to enter: "))
# for i in range(1,n+1):
#     pid = int(input(f"Enter the {i} product ID: "))
#     pname = input(f"Enter the {i} product name: ")
#     price = float(input(f"Enter the {i} price of the product: "))
#     val=(pid,pname,price)
#     curr.execute("INSERT INTO Product VALUES(%s,%s,%s)",val)
#     mydb.commit()
#     print("Product added!")
    


while(True):
    print("1. Insert other products: ")
    print("2. Display: ")
    print("3. Update (product price by id): ")
    print("4. Delete product by id: ")
    print("5. Max product price: ")
    print("6. Total products: ")
    print("0. EXIT: ")
    
    ch = int(input("Enter your choice: "))
    
    match ch:
        case 1:
            pid = int(input(f"Enter the  product ID: "))
            pname = input(f"Enter the  product name: ")
            price = float(input(f"Enter the price of the product: "))
            val=(pid,pname,price)
            curr.execute("INSERT INTO Product VALUES(%s,%s,%s)",val)
            mydb.commit()
            print("Product added!!!")
        
        case 2:
            curr.execute("SELECT * FROM Product")
            for row in curr.fetchall():
                print(row)
                
        case 3:
            pid = int(input(f"Enter the  product ID: "))
            price = float(input(f"Enter the price of the product: "))
            val = (price,pid)
            curr.execute("UPDATE Product SET Pprice=%s WHERE Pid=%s",val)
            mydb.commit()
            print(pid," Price Updated!")
            
        case 4:
            pid = int(input(f"Enter the  product ID: "))
            curr.execute("DELETE FROM Product WHERE Pid=%s",(pid,))
            mydb.commit()
            print(pid," DELETED!!")
            
        case 5:
            curr.execute("SELECT MAX(Pprice) from Product")
            maxp = curr.fetchone()
            print("Max price of the product is ",maxp[0])

        case 6:
            curr.execute("SELECT COUNT(*) FROM Product")
            cnt = curr.fetchone()
            print("TOTAL PRODUCTS ARE :", cnt[0])
            
        case 0:
            print("Exiting..")
            break
