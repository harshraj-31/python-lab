"""

#1. Print Hello World
print("Hello World")

#2. User input
name = input("Enter name: ")
print(name)

#3. Take numerical input
n = int(input("Enter number: "))
print(n)

#4. Convert number to float
n = int(input())
print(float(n))

#5. Add, Subtract, Multiply, Divide
a = int(input())
b = int(input())
print(a+b, a-b, a*b, a/b)

#6. Quotient and Remainder
print(a//b, a%b)

#7. Meter to Kilometer
m = float(input())
print(m/1000)

#8. Area of Rectangle
l = float(input())
b = float(input())
print(l*b)

#9. Volume of Cube
l = float(input())
b = float(input())
h = float(input())
print(l*b*h)

#10. Area of Triangle
b = float(input())
h = float(input())
print((b*h)/2)

#11. Fahrenheit to Celsius
f = float(input())
print((f-32)/1.8)

#12. Celsius to Fahrenheit
c = float(input())
print((c*9/5)+32)

#13. Decimal to Binary, Octal, Hexadecimal
n = int(input())
print(bin(n), oct(n), hex(n))

#14. Binary/Octal/Hexadecimal to Decimal
n = input()
print(int(n,0))

#15. Display data types
a = input()
b = int(input())
c = float(input())
print(type(a), type(b), type(c))

#16. Binary AND & OR
a = int(input())
b = int(input())
print(a & b, a | b)

#17. Area of Circle
r = float(input())
print(3.14*r*r)

#18. Simple Interest
p = float(input())
r = float(input())
n = float(input())
print((p*r*n)/100)

#19. Even or Odd without condition
n = int(input())
print(n%2==0)

#20. Swap two numbers
a = int(input())
b = int(input())
a,b = b,a
print(a,b)

"""