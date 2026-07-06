n = int(input("Enetr the total number of students: "))
students = {}

for i in range(n):
  name = input("Enetr the name: ")
  mark1 = float(input("Enter 1st mark: "))
  mark2 = float(input("Enter 2nd mark: "))
  mark3 = float(input("Enter 3rd mark: "))
  students[name] = [mark1, mark2, mark3]

stud_name = input("Enter student name to get average score: ")
marks = students[stud_name]
stud_average = sum(marks) / len(marks)
print(f"The average marks of {stud_name} is:  {stud_average:.2f}")
