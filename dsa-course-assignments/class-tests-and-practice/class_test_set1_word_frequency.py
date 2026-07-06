# Q1: Display words that appear more than once

sentence = input("Enter a sentence: ")

# Convert sentence to lowercase and split into words
words = sentence.lower().split()

# Dictionary to store word frequency
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Words appearing more than once:")

for word, count in freq.items():
    if count > 1:
        print(f"{word} - {count}")

# Q2: Electricity bill calculation

# Dictionary storing unit ranges and rates
rates = {
    (0, 100): 3.00,
    (101, 200): 4.50,
    (201, 300): 6.00,
    (301, 100000): 8.00
}

units = int(input("Enter total units consumed: "))

bill = 0
remaining_units = units

for (lower, upper), rate in rates.items():
    if remaining_units > 0:
        if units >= lower:
            applicable_units = min(remaining_units, upper - lower + 1)
            bill += applicable_units * rate
            remaining_units -= applicable_units

print("Total Electricity Bill = ₹", bill)

# Q3: Compare two sets

set1 = set(map(int, input("Enter elements of Set 1 separated by space: ").split()))
set2 = set(map(int, input("Enter elements of Set 2 separated by space: ").split()))

if set1 == set2:
    print("Both sets are equal")

elif set2.issubset(set1):
    print("Set 2 is the subset of Set 1")

elif set1.issubset(set2):
    print("Set 1 is the subset of Set 2")

else:
    print("Different sets")