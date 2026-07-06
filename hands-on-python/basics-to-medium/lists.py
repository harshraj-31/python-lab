#39
"""
L1 = ["Amit", "Neha", "Riya", "Amit", "Karan"]

# a. Count total number of students
print("Total students:", len(L1))

# b. Add one more student
L1.append("Pooja")
print("After adding student:", L1)

# c. Display students in sorted order
print("Sorted list:", sorted(L1))

# d. Check a particular student's name
name = input("Enter student name to search: ")
if name in L1:
    print(name, "is present in the list")
else:
    print(name, "is not present in the list")

# e. Count same name students & position of first occurrence
if name in L1:
    print("Total occurrences:", L1.count(name))
    print("Position of first occurrence:", L1.index(name))

# f. Remove last student
L1.pop()
print("After removing last student:", L1)

# g & h. Remove a particular student (all occurrences)
remove_name = input("Enter student name to remove: ")
L1 = [student for student in L1 if student != remove_name]
print("Updated list:", L1)

"""

"""
#40:
nums = [12, 45, 7, 89, 23, 56, 90, 34, 10, 67]

print("Maximum number:", max(nums))
print("Minimum number:", min(nums))



#41
alphabets = ['a', 'b', 'e', 'i', 'o', 'u', 'k']
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for ch in alphabets:
    if ch in vowels:
        count += 1

print("Total vowels:", count)


#42
even_numbers = list(range(2, 22, 2))
print("Even numbers:", even_numbers)


#43
employees = [
    ["Amit", 25, 30000, "Python"],
    ["Neha", 28, 35000, "Java"],
    ["Riya", 26, 32000, "Data Science"]
]

name = input("Enter employee name: ")
found = False

for emp in employees:
    if emp[0] == name:
        print("Employee Details:", emp)
        found = True
        break

if not found:
    print("Employee not found")


#44
L = []
for i in range(5):
    val = input("Enter value: ")
    L.append(val)

print("User list:", L)


#45

for student in L1:
    if 'a' in student.lower():
        print(student)


#46
numbers = [1,2,3,4,5,6,7,8,9,10]

odd_sum = 0
even_sum = 0

for n in numbers:
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

print("Total of even numbers:", even_sum)
print("Total of odd numbers:", odd_sum)


#47
odd_list = []
even_list = []

for n in numbers:
    if n % 2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

print("Even numbers list:", even_list)
print("Odd numbers list:", odd_list)


#48 (without list comprehension)
mixed = [10, "Hello", 25, "Python", 40]

for item in mixed:
    if type(item) == int:
        print(item)
        
        
#with list comprehension
int_list = [item for item in mixed if type(item) == int]
print("Integer elements:", int_list)

"""
