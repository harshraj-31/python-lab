# Q1: Exam Processing System

def Exam_Process(filename):

    total_students = 0
    pass_count = 0
    fail_count = 0

    input_file = open(filename, "r")
    output_file = open("result_students.txt", "w")

    for line in input_file:

        data = line.strip().split(",")

        roll = data[0]
        name = data[1]

        marks = list(map(int, data[2:]))

        total = sum(marks)
        percentage = total / len(marks)

        # Check fail condition
        result = "PASS"

        for m in marks:
            if m < 23:
                result = "FAIL"
                break

        # Update statistics
        total_students += 1

        if result == "PASS":
            pass_count += 1
        else:
            fail_count += 1

        # Write to output file
        output_file.write(
            f"{roll}, {name}, {round(percentage,2)}, {result}\n"
        )

    input_file.close()
    output_file.close()

    # Display statistics
    print("Total Students:", total_students)
    print("PASS:", pass_count)
    print("FAIL:", fail_count)


# Function call
Exam_Process("students_data.txt")

# Q2: Inventory Management System

def add_product():
    name = input("Enter product name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    file = open("inventory.txt", "a")
    file.write(f"{name},{qty},{price}\n")
    file.close()

    print("Product added successfully.")


def view_inventory():

    file = open("inventory.txt", "r")

    print("\nInventory List:")

    for line in file:
        data = line.strip().split(",")
        print(
            "Product:", data[0],
            "Quantity:", data[1],
            "Price:", data[2]
        )

    file.close()


def update_stock():

    name = input("Enter product name to update: ")
    new_qty = input("Enter new quantity: ")

    lines = []

    file = open("inventory.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if data[0] == name:
            data[1] = new_qty

        lines.append(",".join(data))

    file.close()

    file = open("inventory.txt", "w")

    for l in lines:
        file.write(l + "\n")

    file.close()

    print("Stock updated.")


# Menu-driven system

while True:

    print("\nINVENTORY MENU")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Update Stock")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_inventory()

    elif choice == "3":
        update_stock()

    elif choice == "4":
        break

    else:
        print("Invalid choice")