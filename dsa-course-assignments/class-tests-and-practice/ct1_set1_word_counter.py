# Q1: Word Counter in a Sentence

sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Count number of words
print("Total number of words:", len(words))

# Check if a word exists
search_word = input("Enter word to search: ")

if search_word in words:
    print("The word exists in the sentence.")
else:
    print("The word does not exist in the sentence.")

# Q2: Shopping Cart Billing System

# Product dictionary
products = {
    "Apple": 50,
    "Banana": 20,
    "Mango": 30
}

total_bill = 0

while True:

    item = input("Enter product name (or 'done' to finish): ")

    if item.lower() == "done":
        break

    if item in products:

        qty = int(input("Enter quantity: "))

        price = products[item] * qty

        total_bill += price

        print("Added to cart. Cost =", price)

    else:
        print("Product not found.")

print("Total Bill =", total_bill)

# Q3: Triangle Type Determination

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check triangle validity
if a + b <= c or a + c <= b or b + c <= a:
    print("Not a Triangle")

elif a == b == c:
    print("Equilateral Triangle")

elif a == b or b == c or a == c:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")