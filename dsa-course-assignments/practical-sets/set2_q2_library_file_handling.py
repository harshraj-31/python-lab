# Library File Handling
books = []

for i in range(5):
    bid = input("Book ID: ")
    name = input("Book Name: ")
    authors = input("Authors (comma): ")
    price = float(input("Price: "))
    pub = input("Publication: ")
    category = input("Category: ")

    books.append((bid, name, authors, price, pub, category))

file = open("Library.txt", "w")

for b in books:
    file.write(str(b) + "\n")

file.close()

category_count = {}

for b in books:
    cat = b[5]
    category_count[cat] = category_count.get(cat, 0) + 1

print("Books per category:", category_count)

highest = max(books, key=lambda x: x[3])

print("Book with highest price:", highest)

print("Books with one author:")

for b in books:
    if "," not in b[2]:
        print(b)