# Initial student dictionary
stud = {
    1: {"name": "Amit", "age": 23,
        "marks": [(10, 15, 12), (11, 12, 13)]},

    2: {"name": "Bhumi", "age": 22,
        "marks": [(13, 15, 11), (10, 10, 13)]},

    3: {"name": "Bharat", "age": 23,
        "marks": [(12, 12, 14), (13, 14, 15)]}
}


# Function to calculate result
def calculate_result(marks):
    attempt1, attempt2 = marks

    max_marks = []

    for i in range(3):
        max_marks.append(max(attempt1[i], attempt2[i]))

    total = sum(max_marks)
    percentage = total / 3

    return max_marks, percentage


# Function to add new student
def addStud():
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    print("Enter marks for Attempt 1:")
    a1 = tuple(map(int, input(
        "Enter 3 subject marks separated by space: ").split()))

    print("Enter marks for Attempt 2:")
    a2 = tuple(map(int, input(
        "Enter 3 subject marks separated by space: ").split()))

    stud[roll] = {
        "name": name,
        "age": age,
        "marks": [a1, a2]
    }

    print("Student added successfully.")


# Function to display result of one student
def Result(name):
    found = False

    for s in stud.values():
        if s["name"].lower() == name.lower():
            found = True

            max_marks, percentage = calculate_result(s["marks"])

            print("\nResult of", s["name"], "is:")
            print("--------------------------------")

            print("Maximum marks of all 3 subjects are:")
            print(max_marks)

            print("Percentage =", round(percentage, 2))

            print("***********************************")

    if not found:
        print("Student not found.")


# Function to display result of all students
def Report():
    for s in stud.values():

        max_marks, percentage = calculate_result(s["marks"])

        print("\nResult of", s["name"], "is:")
        print("--------------------------------")

        print("Maximum marks of all 3 subjects are:")
        print(max_marks)

        print("Percentage =", round(percentage, 2))

        print("***********************************")


# Menu-driven program
while True:

    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Result of specific student")
    print("3. Report of all students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addStud()

    elif choice == "2":
        name = input("Enter student name: ")
        Result(name)

    elif choice == "3":
        Report()

    elif choice == "4":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")