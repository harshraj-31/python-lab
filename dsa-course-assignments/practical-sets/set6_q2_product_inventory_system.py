# SET-6 Q2: Product Inventory System

products = []

# Function to input product details
def input_products():

    for i in range(5):

        pid = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        supplier = input("Supplier Name: ")

        products.append(
            [pid, name, price, quantity, supplier]
        )


# Function to store data in file
def store_file():

    file = open("Product_Inventory.txt", "w")

    for p in products:
        file.write(str(p) + "\n")

    file.close()

    print("\nData stored in Product_Inventory.txt")


# Function to find most expensive product
def most_expensive():

    expensive = max(products, key=lambda x: x[2])

    print("\nMost expensive product:")
    print(expensive)


# Function to display low quantity products
def low_quantity():

    print("\nProducts with quantity less than 10:")

    for p in products:
        if p[3] < 10:
            print(p)


# Function to calculate total inventory value
def total_inventory_value():

    total = 0

    for p in products:
        value = p[2] * p[3]
        total += value

    print("\nTotal inventory value:", total)


# Function to count products by supplier
def supplier_count():

    count = {}

    for p in products:

        supplier = p[4]

        if supplier in count:
            count[supplier] += 1
        else:
            count[supplier] = 1

    print("\nProducts supplied by each supplier:")
    print(count)


# Main program
input_products()

store_file()

most_expensive()

low_quantity()

total_inventory_value()

supplier_count()