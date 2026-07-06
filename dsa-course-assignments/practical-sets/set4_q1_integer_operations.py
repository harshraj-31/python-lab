# Integer Operations
numbers = []

n = int(input("Enter number of values: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


prime_dict = {}

for num in numbers:
    prime_dict[num] = is_prime(num)

print("Prime dictionary:", prime_dict)

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

digits = set()

for num in numbers:
    for d in str(num):
        digits.add(d)

print("Unique digits:", digits)

result = []

for num in numbers:
    rev = int(str(num)[::-1])
    result.append(num * rev)

print("Multiply by reverse:", result)