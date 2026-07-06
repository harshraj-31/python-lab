import math

#1 print("Hello World")

#2
"""
name = input("Enter your name: ")
print(name)
"""

#3
"""
num = eval(input("Enter the number: "))
print(num)
"""

#4.	Convert the number to floating point number
"""
num = 74
print(float(num))
"""
#5.	WAP to Add, Subtract, Multiply and Divide 2 numbers
#6.	Print the quotient and remainder separately for division operation
"""
num1 = eval(input("Enter the first num:"))
num2 = eval(input("Enter the second num:"))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print("Quotient: ",num1 // num2)
print("Remainder:" num1 % num2) 
"""

#7.	Write a program to find meter to kilometer.
"""
meter = 1900
km = meter / 1000
print("kilometer is : ",km)
"""
#8.	Write a program to find area of a rectangle. (Area=l*b). Take input parameters from user
"""
l = 12.8
b = 9.2
area = l*b
print("Area of rectangle",round(area,2)) #used round function for 2 decimal points
"""

#9.	Write a program to find volume of cube. (Area=l*b*h). Take input parameters from user
"""
l = 12.8
b = 9.2
h = 27.1
area = l*b*h
print("Area of cube: ",area)
"""

#10.	Write a program to find area of triangle. (Area=(l*b)/2). Take input parameters from user
"""
l = 12.8
b = 9.2
area = (l*b) / 2
print("Area of Triangle: ",round(area,2))
"""

#11.	WAP to convert the given temperature from Fahrenheit to Celsius using the formula C = (F – 32) / 1.8
"""
f = eval(input("Enter the fahrenheit: "))
c = (f - 32) / 1.8
print(" Celsuis is:  ",c)
"""

#12.	WAP to convert temperature from Celsius to Fahrenheit where temperature in Celsius is entered by user.
#(F= C*(9/5) + 32)
"""

c= eval(input("Enter the celsius: "))
f= c*(9/5) + 32
print(" fahrenheit is:  ",f)
"""

#13.	Take a number as user input and convert it into Binary, Octal and Hexadecimal numbers
"""
num = eval(input("Enter the number: "))

print("Binary =", bin(num)[2:])
print("Octal =", oct(num)[2:])
print("Hexadecimal =", hex(num)[:2].upper()) #[2:] removes prefixes (0b, 0o, 0x)
"""
#14.	Take binary, octal and hexadecimal numbers as an input and convert them to Decimal number
"""
binary = input("Enter a binary number: ")
octal = input("Enter an octal number: ")
hexa = input("Enter a hexadecimal number: ")

print("Binary to Decimal =", int(binary, 2))
print("Octal to Decimal =", int(octal, 8))
print("Hexadecimal to Decimal =", int(hexa, 16))
"""
#15.	Take 3 different inputs from user and display their data type.
"""
inp1 = input("Enter the input 1: ")
inp2 = eval(input("Enter the input 2: "))
inp3 = int(input("Enter the input 3: "))
print(type(inp1))
print(type(inp2))
print(type(inp3))
"""

#16.	Perform binary “AND” and “OR” operation for given 2 integer numbers from user input
"""
a = 74
b = 21

print("Bitwise AND =", a & b)
print("Bitwise OR =", a | b)

#logial operator: and / or
#binary and/ or = & / |
"""

#17.	Write a program to calculate area of circle. (pi*r*r)
"""
r = eval(input("Enter first number: "))

area = math.pi * r*r
print("area of circle: ",area)
"""

#18.	Write a program to calculate simple interest using formula SI = (P*R*N) / 100. Take all parameters as input from user
"""
p = float(input("Enter principal: "))  #principle amt
r = float(input("Enter rate: "))    #rate of interest
t = float(input("Enter time (years): "))  # time

si = (p * r * t) / 100

print("Simple Interest =", si)
"""
#19.	Without applying condition statement display output as “true” if a number is an even number and “false” if the number is an odd number
"""
num = 24
print(num%2==0)
"""

#20.	Write a program to swap two numbers using a third variable and also without using the third variable.
"""
a = 12
b = 23
#using 3rd variable

c = a
a = b
b = c
print(a)
print(b)
"""
#w/o using third variable
"""
a,b = b,a
print(a)
print(b)
"""

#21.	Write a program to display the operations of bitwise AND  and bitwise OR on two numbers entered by the user
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Bitwise AND =", a & b)
print("Bitwise OR =", a | b)
"""

#22.	Find the output for the following code
#23.
"""
x=0
y=200
print(x and y)  # if the value is first value is zero then 0 otherwise second value
print (x or y)   # always first non-zero value
# Update the values of x and y to 0 and then check the output again. Analyse the result in regards to python
"""

"""
1.	Find the minimum and maximum of 2 numbers

num1 = 12
num2= 14
print("Maximum: ",num1 if num1>num2 else num2)
print("Minimum: ",num1 if num1<num2 else num2)
"""

"""
2.	Write a program to find the maximum of three numbers
num1 = 122
num2= 145
num3 = 87
if num1 > num2 and num1 > num3:
    print("Maximum: ",num1)
elif num2 > num3:
    print("Maximum: ", num2)
else:
    print("Maximum: ",num3)
"""

"""
3.	Write a program to input the basic salary and calculate the net salary based on the given conditions. If basic is <10000 then da=25%, hra=5%. If basic>=10000 and basic <=30000 then da=35%, hra=10%. If basic >30000 then da=40%, hra=20%. Pf is same for all 12%.

basic = float(input("Enter basic salary: "))

if basic < 10000:
    da = basic * 0.25
    hra = basic * 0.05
elif basic <= 30000:
    da = basic * 0.35
    hra = basic * 0.10
else:
    da = basic * 0.40
    hra = basic * 0.20

pf = basic * 0.12

net = basic + da + hra - pf

print("Net Salary =", net)
"""
"""
4.	Print 1 to 10 numbers in ascending and descending order using range 

for i in range(1,11):
    print(i)
"""
"""
5.	Print odd numbers between 1 to 50

print("Odd Numbers: ")
for i in range(1,51,2):
    print(i)
"""

"""
6.	Print the ‘*’ patterns using range()

for i in range(1,6):
    print(i * "*")
"""

"""

7.	Print the number pyramid using range()

rows = 5

for i in range(1, rows + 1):
    # print spaces
    for j in range(rows - i):
        print(" ", end="")
    # print odd count numbers in order
    for k in range(1, 2 * i):
        print(k, end="")

    print()
"""
"""
8.	Print all prime numbers between 10 to 50

for num in range(10, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime and num > 1:
        print(num, end=" ")
"""
"""
9.	Take 10 numbers (min 3 digits) as user input and check whether a number is palindrome or not.
count = 0
while count < 10:
    num = input(f"Enter the {count + 1} number: ")

    if len(num) < 3:
        print("Numbers have less than 3 digits")
        continue

    if num == num[::-1]: # [::-1] used for reverse
        print(num, "Is palindrome")
    else:
        print(num, "Is not palindrome")

    count = count + 1
"""
"""
10.	WAP to check whether the given number is Armstrong or not.

num = int(input("Enter a number: "))

temp = num
power = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")
"""
"""

11.	WAP to input n numbers and count the total number of odd and even numbers in the tuple.

tup = tuple(i for i in range(1,20))
oddcnt = 0
evencnt = 0
for i in tup:
    if i % 2 == 0:
        evencnt += 1
    else:
        oddcnt += 1

print("Even numbers count",evencnt)
print("Odd numbers count",oddcnt)

"""

"""
12.	Print multiple lines using single print statement. as – 
                     I like “Python Programming” very much
                     It is my favorite subject
13.	Print a part of the above string “very much” using the slice operator. 
14.	Print the last 5 characters from the above given string
15.	Print only the second line of the given string
"""

line = """I like "Python Programming" very much
It is my favorite subject
practicing python"""

#print(line[27:37])
#print(line[-5:])
#print(line[37:63])
"""


16.	Take two strings as input from the user and concatenate them.

str1 = "Hello"
str2 = "Print"

print(str1+str2)
"""

"""
17.	Take a number and a string from the user and repeat the string for that many times.

str1 = input("Enter the string: ")
times = int(input("Enter the number of times you want to repeat: "))
print(str1 * times)
"""
"""
18.	Take an input character from the user and check whether that character is present in the above given string or not. – Using ‘in’ operator and using ‘not in’ operator

mainstr = "Hello print"
str1 = input("Enter the character to find: ")
print("present" if str1 in mainstr else "Not present")
"""

"""
19.	Create a menu driven program for string manipulation
a.	Find the length of a string
b.	Print the string in upper case
c.	Print the string in lower case
d.	Print the string with initial capital
e.	Split the string based on the character entered.


str1 = input("Enter the string: ")
while True:
    print("1.Find the length of a string")
    print("2.Print the string in upper case")
    print("3.Print the string in lower case")
    print("4.Print the string with initial capital")
    print("5.Split the string based on the character entered.")
    ch = int(input("Enter the choice: "))
    match ch:
        case 1:
            print(len(str1))

        case 2:
            print(str1.upper())

        case 3:
            print(str1.lower())

        case 4:
            print(str1.capitalize())

        case 5:
            char = input("Enter the character to split the string: ")
            splt = str1.split(char)
            for i in splt:
                print(i)

        case 0:
            exit(0)
"""

"""
20.	Take two strings as input s1 and s2 and check whether s2 is present in s1 or not.
21.	If s2 is a part of s1 then print the 1st and last occurrences of it 
22.	If s2 is present in s1 then also count number of times it occurs in s1.
23.	Count total number of words in the string input by user 
24.	Take a string input from user and print it in reverse using range 



# Take main string input from the user
s1 = input("Enter main string (s1): ")

# Take substring input from the user
s2 = input("Enter substring (s2): ")

# Check whether s2 exists inside s1
if s2 in s1:
    print("s2 is present in s1")

    # find() searches from LEFT to RIGHT
    # It returns the index (position) of the FIRST occurrence of s2 in s1
    # Indexing starts from 0
    # If substring is not found, find() returns -1
    first = s1.find(s2)

    # rfind() searches from RIGHT to LEFT
    # It returns the index of the LAST occurrence of s2 in s1
    # Still returns the position counted from the left (starting at 0)
    # If substring is not found, rfind() returns -1
    last = s1.rfind(s2)

    # Print positions
    print("First occurrence index:", first)
    print("Last occurrence index:", last)

    # count() returns how many times s2 appears in s1
    count = s1.count(s2)
    print("Number of times s2 occurs:", count)

else:
    # Runs if s2 does not exist in s1
    print("s2 is NOT present in s1")

# split() breaks the string into words using spaces by default
# It returns a list of words
words = s1.split()

# len() counts how many words are in that list
print("Total number of words in s1:", len(words))

"""

"""
25.	Take a tuple input and print all the elements of it in reverse sequence

tup = (1,2,3,4,5)
for i in reversed(tup):
    print(i)
"""


"""
26.	Copy the inputted string to another string by replacing the character 
‘o’ with ‘@’ Eg. ‘Hello’ will be copied to another string as 
‘Hell@’ and ‘Good Morning’ will become ‘G@@d M@rning’ (Without using replace())

# Take input string from user
s = input("Enter a string: ")

# Create empty string for result
new_string = ""

# Traverse each character in the original string
for ch in s:
    # If character is 'o', add '@' to new string
    if ch == 'o':
        new_string = new_string + '@'
    else:
        # Otherwise copy the same character
        new_string = new_string + ch

# Print copied modified string
print("New string:", new_string)
"""

"""
27.	Take a string as an input from the user. Find total number of vowels in it. (Hint: take a tuple of vowels)

s = input("Enter the string: ")
vowels = ("a","e","i","o","u")
vcount = 0
for i in s.lower():
    if i in vowels:
        vcount += 1
        
print("Total Vowels: ", vcount)
"""

"""
28.	Create a tuple for name say t1 (FirstName, MiddleName, LastName)
29.	Create a tuple say t2 for marks of 5 subjects 
30.	Make a total of all the marks and print it. (with and without using sum() method)
31.	Make a tuple t3 having 2 elements as t1 and t2 (tuples created above) – It is called a nested tuple
32.	Take an input number and find whether that is present as an element in the tuple t3 or not.

t1 = ("James","Arthur","Bond")
t2 = (81,69,97,89,74)
totalMarks = 0

for i in t2:
    totalMarks += i

print(" without using sum()method: ",totalMarks) # without using sum()method

print(" with using sum()method", sum(t2))

t3 = (t1,t2)
print("Nested Tuple: ",t3)

num = int(input("Enter a number: "))
if num in t3[0] or num in t3[1]:
    print(num," Present")
else:
    print(num," Not present")

"""
"""
33.	Create a tuple of 5 fruits. Ask the user to input a fruit name and search that name in the given fruit tuple. Display suitable messages

fruits = ("mango","Apple","Banana","Pineapple","Litchi")
inp = input("Enter the fruit name: ")
if inp in fruits:
    print(inp," is present in fruits")
else:
    print(inp,"Not present in fruits")
"""
"""
34.	Create a tuple of cities of Gujarat by taking user input.
35.	Find the length of name of each city in the above tuple. With and without len() method


num = int(input("Enter the number of city you want to input: "))
city = []
for i in range(1,num+1):
    inp = input(f"Enter the city {i} name: ")
    city.append(inp)

gujcity = tuple(city)
print(gujcity)

for word in gujcity:
    count = 0
    for ch in word:
        count += 1
    print(word," Got ", count)
"""
