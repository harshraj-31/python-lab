"""
#1. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Minimum:", min(a,b))
print("Maximum:", max(a,b))

#2. 
a = int(input())
b = int(input())
c = int(input())
print("Maximum:", max(a,b,c))

#3. Net salary calculation
basic = int(input("Enter basic salary: "))
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
print("Net Salary:", basic + da + hra - pf)

#4. Print 1 to 10 ascending and descending
for i in range(1,11):
    print(i)
for i in range(10,0,-1):
    print(i)

#5. P
for i in range(1,51):
    if i % 2 != 0:
        print(i)

#6. pattern
for i in range(1,6):
    print("*" * i)

#7. Print number pyramid
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

#8. 
for n in range(10,51):
    flag = 0
    for i in range(2,n):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        print(n)

#9. Palindrome number
n = input("Enter number: ")
rev = n[::-1]
if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#10. Armstrong number
n = int(input("Enter number: "))
temp = n
sum = 0
while temp > 0:
    d = temp % 10
    sum = sum + d*d*d
    temp = temp // 10
if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")

#11. 
t = (10,21,32,43,54)
even = 0
odd = 0
for i in t:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)

#12. 
print("I like Python Programming very much\nIt is my favorite subject")

#13. 
s = "I like Python Programming very much"
print(s[27:36])

#14. 
print(s[31:36])

#15. 
s = "I like Python Programming very much\nIt is my favorite subject"
print(s[37:63])

#16.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(s1 + s2)

#17. 
n = int(input("Enter number: "))
s = input("Enter string: ")
print(s * n)

#18. 
ch = input("Enter character: ")
print(ch in s)
print(ch not in s)

#19. 
print("Length:", len(s))

#20. 
print(s.upper())
print(s.lower())
print(s.capitalize())

#21.
ch = input("Enter split character: ")
print(s.split(ch))

#22. 
s1 = input("Enter main string: ")
s2 = input("Enter sub string: ")
if s2 in s1:
    print("Present")
else:
    print("Not Present")

#23. 
if s2 in s1:
    print("First:", s1.find(s2))
    print("Last:", s1.rfind(s2))

#24. 
print("Count:", s1.count(s2))

#25
print("Total words:", len(s.split()))

#26. 
s = input("Enter string: ")
print(s[::-1])

#27.
t = (1,2,3,4,5)
print(t[::-1])

#28. 
new = ""
for ch in s:
    if ch == 'o':
        new = new + '@'
    else:
        new = new + ch
print(new)

#29. 
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels:", count)

#30
t1 = ("Amit","Kumar","Shah")

#31. 
t2 = (70,80,90,85,75)
total = 0
for m in t2:
    total += m
print("Total:", total)

#32. 
t3 = (t1, t2)

#33.
n = int(input("Enter number: "))
if n in t3:
    print("Present")
else:
    print("Not Present")

#34.
fruits = ("apple","banana","mango","orange","grapes")
f = input("Enter fruit name: ")
if f in fruits:
    print("Found")
else:
    print("Not Found")

#35.
cities = ("Ahmedabad","Surat","Vadodara")
for c in cities:
    print(c, len(c))

#36.
t4 = ("Amit",("cricket","music"),("Riya","Neha"),"MCA")
if "cricket" in t4[1]:
    print("Found")
else:
    print("Not Found")

#37.
t = (1,2,3,4,5,6,7,8,9,10)
odd = ()
even = ()
for i in t:
    if i % 2 == 0:
        even = even + (i,)
    else:
        odd = odd + (i,)
print("Odd:", odd)
print("Even:", even)

"""