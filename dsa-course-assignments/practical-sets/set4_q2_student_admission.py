# Student Admission
students = []

for i in range(5):
    adm = input("Admission Number: ")
    name = input("Name: ")
    course = input("Course: ")
    paid = float(input("Fees Paid: "))
    total = float(input("Total Fees: "))

    students.append([adm, name, course, paid, total])

file = open("Student_admission.txt", "w")

for s in students:
    file.write(str(s) + "\n")

file.close()

course_count = {}

for s in students:
    c = s[2]
    course_count[c] = course_count.get(c, 0) + 1

print("Students per course:", course_count)

highest = max(students, key=lambda x: x[3])

print("Highest fees paid:", highest)

print("Pending fees:")

for s in students:
    if s[3] < s[4]:
        print(s)

total_collected = sum(s[3] for s in students)

print("Total fees collected:", total_collected)