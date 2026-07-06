
#Prime numbers 1–N:
"""
num = int(input("Enter how much limit to find prime: "))

#logic for prime
for n in range(2, num + 1):
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n)
"""

#PALINDROME
"""
n = int(input("Enter the number: "))
temp = n
rev = 0

#logic for palindrome
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

print("Palindrome" if temp == rev else "Not Palindrome")


#if string
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
"""

#10. Armstrong number (3 digit only)
"""
n = int(input())
temp = n
s = 0

while n > 0:
    d = n % 10
    s += d ** 3
    n //= 10

print("Armstrong" if s == temp else "Not Armstrong")
"""
"""

#logic for pal

nums = [153, 370, 123, 9474, 100]

for n in nums:
    s = str(n)
    power = len(s)
    total = 0

    for d in s:
        total += int(d) ** power

    if total == n:
        print(n, "is Armstrong")
    else:
        print(n, "is Not Armstrong")

dicts = {
    1:"World",
    2:"iS",
    3:"Beautiful"
}

with open("C:/Users/KARAN/OneDrive/Desktop/PYTHON/Theory and materials/PYTHON/PPTS/main.txt","wb") as f:
    f.write()


with open("C:/Users/KARAN/OneDrive/Desktop/PYTHON/Theory and materials/PYTHON/PPTS/main.txt","r") as f:
    print(f.read())
    f.seek(0)
    print(f.readlines())
"""


#LOGIN CHECKER
"""

def create_user_file():
    # Predefined username and password
    uname = input("Enter the username to store: ")
    passw = input("Enter the password to store: ")
    with open("C:/Users/KARAN/OneDrive/Desktop/PYTHON/Theory and materials/PYTHON/PPTS/main.txt", "w") as file:
        file.write(uname+","+passw)  # format: username,password

def login():
    create_user_file()
    with open("C:/Users/KARAN/OneDrive/Desktop/PYTHON/Theory and materials/PYTHON/PPTS/main.txt", "r") as file:
        data = file.read().strip().split(",")
        stored_username = data[0]
        stored_password = data[1]

    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == stored_username and password == stored_password:
            print(f"Welcome {username}!")
            return
        else:
            attempts -= 1
            print(f"Incorrect credentials. Attempts left: {attempts}")
    print("Access blocked. Too many failed attempts.")

# Run Login
login()


#Random word generartor
def writewords():
    with open("C:/Users/KARAN/OneDrive/Desktop/PYTHON/Theory and materials/PYTHON/PPTS/words.txt", "a") as f:
        n = input("Enter 4 character word: ")
        if len(n) < 4 or len(n) > 4:
            print("4 Characters only ")
        else:
            f.write("\n")
            f.write(n)
            print("Added successfully")


import random
# Function to read words from file
def read_words():
    file = open("C:/Users/KARAN/OneDrive/Desktop/PYTHON/Theory and materials/PYTHON/PPTS/words.txt", "r")
    words = file.read().split()
    file.close()
    return words

def random_word():
    character_list = ['a','b','c','d','e','f','g','h','i','j',
                      'k','l','m','n','o','p','q','r','s','t',
                      'u','v','w','x','y','z']

    word = ""
    for i in range(4):
        word += random.choice(character_list)
    return word


def guess_word():
    words = read_words()

    attempts = 3

    while attempts > 0:

        choice = input("Enter 1 to type word OR 2 for random word: ")

        if choice == "1":
            user_word = input("Enter a 4 letter word: ")
        else:
            user_word = random_word()
            print("Random word generated:", user_word)

        if user_word in words:
            print("Success! Word found in file.")
            return
        else:
            attempts -= 1
            print("Try Again. Attempts left:", attempts)

    print("Game Over!")


# Run program
guess_word()

#Smart loan calculator
def loan_calculator():
    # Input with validation
    principal = float(input("Enter loan amount: "))
    if principal <= 0:
        print("Invalid loan amount!")
        return

    years = int(input("Enter number of years: "))
    if years <= 0:
        print("Years must be > 0")
        return
    if years > 30:
        print("Loan tenure exceeds policy limit")
        return

    customer_type = input("Enter customer type (Regular/Senior Citizen): ").strip().lower()

    # Interest rate slabs
    if principal <= 50000:
        rate = 8
    elif principal <= 200000:
        rate = 10
    else:
        rate = 12

    if customer_type == "senior citizen":
        rate -= 1

    # Compound Interest Calculation
    amount = principal * ((1 + rate/100) ** years)
    interest = amount - principal
    emi = amount / (years * 12)

    # Display Output
    print("\n--- Loan Details ---")
    print("Applicable Interest Rate: ",round(rate,2))
    print("Total Interest: ",round(interest,2))
    print("Total Payable Amount: ",round(amount, 2))
    print("Monthly EMI: ",round(emi, 2))

# Run Loan Calculator
loan_calculator()



def multiplication_table():
    while True:
        num = int(input("Enter a number (≤10): "))
        if num <= 10 and num > 0:
            break
        else:
            print("Invalid input. Please enter number ≤ 10.")

    print(f"\nMultiplication Table up to {num}:\n")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

# Run Multiplication Table
multiplication_table()
"""