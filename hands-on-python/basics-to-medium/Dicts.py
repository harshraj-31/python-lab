"""
62.	Create a dictionary of employees where empId will be the key and value will be the name of an employee
1.	Display how many employees are there in the dictionary.
2.	Display all empID and add them in a separate list.
3.	Display all employee names and take them to a separate list
4.	Take an empId from the user and check if that employee is there in the dictionary or not.
5.	If an empID is there in the dictionary then display the name of that employee or if not available then add an ID and Name of the employee in the dictionary
6.	Change the name of the employee of empID taken by the user
7.	Remove an employee whose ID is provided by the user

emp = {
    101: "Amit",
    102: "Neha",
    103: "Rahul",
    104: "Priya"
}

#1
print("Total number of employee: ",len(emp))

#2
emp_ids = list(emp.keys())
print("Employee ID's", emp_ids)

#3
emp_names = list(emp.values())
print("Employee name", emp_names)

#4 & 5
emp_id = int(input("Enter the emp id: "))
if emp_id in emp:
    print("Employee Name: ", emp[emp_id])
else:
    name = input("Enter employee name: ")
    emp[emp_id] = name
    print("Employee added succesfully")
    print(emp)


#6
emp_id = int(input("Enter the Employee id"))
if emp_id in emp:
    new_name = input("Enter the new name: ")
    emp[emp_id] = new_name
    print("name Updated Successfully")
    print(emp)
else:
    print("Employee ID not found")

#7
emp_id = int(input("Enter the employee ID"))
if emp_id in emp:
    del emp[emp_id]
    print("Employee removed")
    print(emp)
else:
    print("Employee ID not found")
"""

"""
63.	  Take 5 names of students as an input from the user and create a dictionary with keys as their initials and value is a list as [age, degree, favorite subject]
1.	Display the youngest student from the above dictionary.
2.	Create a dictionary of students having rollno of the student is as key and value is a list of marks obtained by that student in 5 subjects
3.	Create a dictionary from the above one, where key is rollno and value is (total of all subjects, percentage and grade ) a tuple of his result
4.	Display the rollno who has scored highest marks (total)
5.	Take 10 numbers from the user and create a list, apply bubble sort and arrange the elements in the list.


students = {}

for i in range(3):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    deg = input("Enter the degree: ")
    favsub = input("Enter the favrouite subject: ")
    initials = name[0].upper()
    students[initials] = [age,deg,favsub]

print(students)

youngest_age = 100
youngest_student = ""

for key,value in students.items():
    if value[0] < youngest_age:
        youngest_age = value[0]
        youngest_student = key

print("Youngest student initial: ",youngest_student)
print("Age: ",youngest_age)

`
marks = {}

for i in range(3):
    roll_no = int(input("Enter roll number: "))
    marks_list = []

    for j in range(5):
        mark = int(input("Enter mark: "))
        marks_list.append(mark)

    marks[roll_no] = marks_list


print(marks)



result = {}

for roll in marks:
    total = 0
    for m in marks[roll]:
        total = total + m

    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    result[roll] = (total, percentage, grade)

print(result)

highest_total = 0
topper = 0

for roll in result:
    if result[roll][0] > highest_total:
        highest_total = result[roll][0]
        topper = roll

print("Topper Roll No:", topper)

"""