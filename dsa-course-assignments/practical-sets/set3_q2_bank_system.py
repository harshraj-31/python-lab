# Bank System
customers = []

for i in range(5):
    acc = input("Account Number: ")
    name = input("Name: ")
    acc_type = input("Type: ")
    balance = float(input("Balance: "))

    customers.append([acc, name, acc_type, balance])

file = open("Bank.txt", "w")

for c in customers:
    file.write(str(c) + "\n")

file.close()

count = {}

for c in customers:
    t = c[2]
    count[t] = count.get(t, 0) + 1

print("Customers per type:", count)

highest = max(customers, key=lambda x: x[3])

print("Highest balance:", highest)

for c in customers:
    if c[2].lower() == "saving":
        c[3] = c[3] * 1.05

print("Balances after interest:", customers)

print("Balance less than 5000:")

for c in customers:
    if c[3] < 5000:
        print(c)