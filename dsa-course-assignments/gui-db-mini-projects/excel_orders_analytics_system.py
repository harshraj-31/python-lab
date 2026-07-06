# SET-5: Excel Orders Analytics System

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
CREATE TABLE IF NOT EXISTS orders (
    order_id INT,
    customer_name VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    price FLOAT,
    order_date DATE
)
""")

conn.commit()


# ---------------- READ EXCEL ----------------

def read_excel():

    df = pd.read_excel("orders.xlsx")

    print("\nData from Excel:")
    print(df)

    return df


# ---------------- SAVE TO DATABASE ----------------

def save_to_database():

    df = read_excel()

    for _, row in df.iterrows():

        sql = """
        INSERT INTO orders
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            int(row["OrderID"]),
            row["CustomerName"],
            row["Product"],
            int(row["Quantity"]),
            float(row["Price"]),
            row["OrderDate"]
        )

        cursor.execute(sql, values)

    conn.commit()

    print("\nData saved to database.")


# ---------------- LOAD DATAFRAME ----------------

def load_dataframe():

    df = pd.read_sql_query(
        "SELECT * FROM orders",
        conn
    )

    print("\nData from Database:")
    print(df)

    return df


# ---------------- DISPLAY FUNCTIONS ----------------

def total_revenue_per_product():

    df = load_dataframe()

    df["Revenue"] = df["quantity"] * df["price"]

    result = df.groupby("product")["Revenue"].sum()

    print("\nTotal revenue per product:")
    print(result)


def orders_per_customer():

    df = load_dataframe()

    result = df["customer_name"].value_counts()

    print("\nNumber of orders per customer:")
    print(result)


def filter_orders():

    df = load_dataframe()

    date = input("Enter date (YYYY-MM-DD): ")

    result = df[df["order_date"] > date]

    print("\nOrders after date:")
    print(result)


# ---------------- PLOTS ----------------

def plot_pie():

    df = load_dataframe()

    df["Revenue"] = df["quantity"] * df["price"]

    revenue = df.groupby("product")["Revenue"].sum()

    revenue.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Revenue Contribution by Product")

    plt.ylabel("")

    plt.show()


def plot_bar():

    df = load_dataframe()

    orders = df["customer_name"].value_counts()

    orders.plot(kind="bar")

    plt.title("Number of Orders per Customer")

    plt.xlabel("Customer")

    plt.ylabel("Orders")

    plt.show()


# ---------------- MAIN MENU ----------------

while True:

    print("\nMENU")
    print("1. Read Excel & Save to Database")
    print("2. Total Revenue per Product")
    print("3. Orders per Customer")
    print("4. Filter Orders After Date")
    print("5. Pie Chart (Revenue)")
    print("6. Bar Chart (Orders)")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        save_to_database()

    elif choice == "2":
        total_revenue_per_product()

    elif choice == "3":
        orders_per_customer()

    elif choice == "4":
        filter_orders()

    elif choice == "5":
        plot_pie()

    elif choice == "6":
        plot_bar()

    elif choice == "7":
        break

    else:
        print("Invalid choice")


conn.close()