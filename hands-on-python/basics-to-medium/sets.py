"""
1.	Write a Python program to store student roll numbers in a set and prepare the sets according to the requirement of the question
a.	Write a program to add new students to an existing class attendance set.
b.	Write a program to remove students who are absent from the attendance set.


attendance = {1,2,3,4,5}
#a
attendance.add(7)
print("Before removing absent students")
print(attendance)
#b
absent = {0,3,8,7}
print(attendance - absent)
"""


"""
2.	 Create a sets of Courses and write a program to check whether a given student is enrolled in a particular course or not.
a.	Write a program to find students who are enrolled in both the courses. 

ml = {74,66,59}
py = {74,24,52,66}

print(ml&py," roll numbers were enrolled in both courses")
"""

"""
3.	Create two sets of elective subjects chosen by the students. Write a program to find students who are enrolled in at least one of two elective subjects
a.	Write a program to find students who are enrolled only in Course A and not in Course B.
b.	Write a program to find students who participated in exactly one of two courses.
c.	Write a program to remove duplicate student from course sets.

A = {74,88,44,66}
B = {65,74,45,88}
print("Students enrolled in both courses: ",A & B)
print("students who participated in exactly one of two courses",A^B)
unique_students = A.union(B)
print("Students after removing duplicates:", unique_students)
"""
"""

4.	Given the set
students = {"Amit", "Neha", "Riya", "Karan"}
write a Python program to check whether "Riya" is enrolled in the course.

students = {"Amit", "Neha", "Riya", "Karan"}
if "Riya" in  students:
    print("Present")
else:
    print("Not present")
"""

"""
5.	Given the sets
math_students = {"Amit", "Neha", "Riya"}
cs_students = {"Riya", "Karan", "Pooja"}
write a program to find students enrolled in both subjects.
math_students = {"Amit", "Neha", "Riya"}
cs_students = {"Riya", "Karan", "Pooja"}
print("Students enrolled in both the courses are ",math_students & cs_students)
"""
"""
6.	Given the sets
club_A = {"Rahul", "Sneha", "Amit"}
club_B = {"Sneha", "Karan", "Pooja"}
write a program to find students who are members of at least one club.

club_A = {"Rahul", "Sneha", "Amit"}
club_B = {"Sneha", "Karan", "Pooja"}
print("students who are members of at least one club are: ",club_A ^ club_B)
"""

"""
7.	Given the sets
course_A = {"Amit", "Neha", "Riya", "Karan"}
course_B = {"Neha", "Karan"}
write a program to find students enrolled only in Course A.

course_A = {"Amit", "Neha", "Riya", "Karan"}
course_B = {"Neha", "Karan"}
print("students enrolled only in Course A are: ",course_A - course_B)
"""

"""
8.	Given the sets
workshop1 = {"Amit", "Riya", "Pooja"}
workshop2 = {"Riya", "Karan", "Neha"}
write a program to find students who attended exactly one workshop.

workshop1 = {"Amit", "Riya", "Pooja"}
workshop2 = {"Riya", "Karan", "Neha"}
print("students who attended exactly one workshop are: ",workshop1 ^ workshop2)
"""

"""
9.	Given the set
attendance = {"Amit", "Neha", "Riya", "Karan"}
write a program to remove "Neha" from the attendance list.

attendance = {"Amit", "Neha", "Riya", "Karan"}
attendance.difference_update(["Riya"])
print(attendance)
"""

"""
10.	Given the set
present_students = {"Ravi", "Sneha", "Amit"}
write a program to display all students using a loop.

present_students = {"Ravi", "Sneha", "Amit"}
for i in  present_students:
    print(i)'
"""

"""
11.	Given the list
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
write a program to remove duplicate email IDs using a set.

emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
newemail = set(emails)
print(newemail)
"""

"""
12.	Given the sets
class_A = {"Amit", "Neha"}
class_B = {"Amit", "Neha", "Riya", "Karan"}
write a program to check whether Class A is a subset of Class B.

class_A = {"Amit", "Neha"}
class_B = {"Amit", "Neha", "Riya", "Karan"}
print(class_A.issubset(class_B))
"""

"""
13.	Given the sets
team1 = {"Amit", "Riya"}
team2 = {"Karan", "Neha"}
write a program to check whether the two teams are disjoint.

team1 = {"Amit", "Riya"}
team2 = {"Karan", "Neha"}
print(team1.isdisjoint(team2))
"""