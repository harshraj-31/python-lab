# Q1: String operations

def string_operations(s):

    # Reverse string
    print("Reverse:", s[::-1])

    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    print("Vowels:", v_count)
    print("Consonants:", c_count)

    # Palindrome check
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

    # Replace vowels
    modified = ""
    for ch in s:
        if ch in vowels:
            modified += "*"
        else:
            modified += ch

    print("Modified string:", modified)


text = input("Enter a string: ")
string_operations(text)

# Q2: Hotel Reservation System

rooms = [
    {"room_no": 101, "type": "AC", "price": 2000, "available": True},
    {"room_no": 102, "type": "Non-AC", "price": 1500, "available": True},
    {"room_no": 103, "type": "AC", "price": 2500, "available": False}
]

def display_available():
    for r in rooms:
        if r["available"]:
            print(r)

def room_type_search(rtype):
    for r in rooms:
        if r["type"] == rtype:
            print((r["room_no"], r["price"]))

def max_price_room():
    max_price = max(r["price"] for r in rooms)
    for r in rooms:
        if r["price"] == max_price:
            print(r)

def book_room(room_no):
    for r in rooms:
        if r["room_no"] == room_no:
            if r["available"]:
                r["available"] = False
                print("Room booked")
            else:
                print("Room not available")


display_available()
room_type_search("AC")
max_price_room()
book_room(101)

# Q3: Prime check and table

num = int(input("Enter number: "))

is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
else:
    print("Not prime")

# Q4: Word operations

sentence = input("Enter sentence: ")

words = sentence.split()

print("All words:", words)

unique_words = set(words)

print("Unique words:", unique_words)

print("Count of unique words:", len(unique_words))

# Q5: Library Management

books = []

n = int(input("Enter number of books: "))

for i in range(n):
    book = {
        "id": input("Book ID: "),
        "name": input("Book Name: "),
        "author": input("Author: "),
        "category": input("Category: "),
        "copies": int(input("Copies: "))
    }
    books.append(book)


def display_category(cat):
    for b in books:
        if b["category"] == cat:
            print(b)


def max_copies():
    max_val = max(b["copies"] for b in books)
    for b in books:
        if b["copies"] == max_val:
            print(b)


def low_copies(limit):
    for b in books:
        if b["copies"] < limit:
            print(b["author"])


def issue_book(book_id):
    for b in books:
        if b["id"] == book_id:
            if b["copies"] > 0:
                b["copies"] -= 1
                print("Book issued")
            else:
                print("No copies available")


display_category(input("Enter category: "))
max_copies()
low_copies(int(input("Enter limit: ")))
issue_book(input("Enter book ID: "))

print("Updated books:")
for b in books:
    print(b)

# Q6: Number palindrome

num = int(input("Enter number: "))

if str(num) == str(num)[::-1]:
    print("Palindrome")

    for i in range(1, num + 1):
        print(i)
else:
    print("Not palindrome")

# Q7: Word repetition and palindrome words

text = input("Enter string: ")

words = text.split()

freq = {}

palindrome_count = 0

for w in words:
    freq[w] = freq.get(w, 0) + 1

    if w == w[::-1]:
        palindrome_count += 1

print("Word frequency:")
for k, v in freq.items():
    print(k, ":", v)

print("Number of palindrome words:", palindrome_count)

# Q8: Employee Management

employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    emp = {
        "id": input("Employee ID: "),
        "name": input("Name: "),
        "dept": input("Department: "),
        "salary": float(input("Basic salary: "))
    }
    employees.append(emp)


def gross_salary():
    for e in employees:
        gs = e["salary"] + (0.2 * e["salary"])
        print(e["name"], "Gross salary:", gs)


def highest_salary():
    max_sal = max(e["salary"] for e in employees)
    for e in employees:
        if e["salary"] == max_sal:
            print(e)


def update_salary(emp_id, new_salary):
    for e in employees:
        if e["id"] == emp_id:
            e["salary"] = new_salary


def count_department():
    dept_count = {}
    for e in employees:
        dept = e["dept"]
        dept_count[dept] = dept_count.get(dept, 0) + 1

    print(dept_count)


gross_salary()
highest_salary()
update_salary(input("Enter ID: "), float(input("New salary: ")))
count_department()

# Q9: Sum of digits of 3-digit numbers

n = int(input("Enter number of values: "))

result = {}

for i in range(n):
    num = int(input("Enter 3-digit number: "))

    s = 0
    temp = num

    while temp > 0:
        s += temp % 10
        temp //= 10

    result[num] = s

print("Dictionary:")
print(result)