# Q1: Check Palindrome

string = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
string = string.lower()

if string == string[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is NOT a Palindrome")

# Q2: Unique sorted numbers from mixed input

data = input("Enter comma separated values: ")

items = data.split(",")

numbers = []

for item in items:
    item = item.strip()
    if item.isdigit():   # check if numeric
        numbers.append(int(item))

# Remove duplicates and sort
unique_numbers = sorted(set(numbers))

print(unique_numbers)

# Q3: Check Anagram

str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

# Remove spaces if any
str1 = str1.replace(" ", "")
str2 = str2.replace(" ", "")

if sorted(str1) == sorted(str2):
    print("S1 and S2 are Anagrams")
else:
    print("Not Anagrams")    