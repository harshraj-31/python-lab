# Number Operations
numbers = []

n = int(input("Enter number of values: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

digit_dict = {}

for num in numbers:
    digit_dict[num] = len(str(num))

print("Digit dictionary:", digit_dict)

palindromes = []

for num in numbers:
    if str(num) == str(num)[::-1]:
        palindromes.append(num)

print("Palindrome numbers:", tuple(palindromes))

digit_sum = 0

for num in numbers:
    for d in str(num):
        digit_sum += int(d)

print("Sum of digits:", digit_sum)

multiplied = []

for num in numbers:
    multiplied.append(num * 10)

print("Numbers multiplied by 10:", multiplied)