# Medical Store File Handling
medicines = []

for i in range(5):
    mid = input("Medicine ID: ")
    name = input("Medicine Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    total = price * qty

    medicines.append((mid, name, price, qty, total))

file = open("medical_store.txt", "w")

for m in medicines:
    file.write(str(m) + "\n")

file.close()

highest = max(medicines, key=lambda x: x[4])

print("Medicine with highest stock value:", highest)

total_value = sum(m[4] for m in medicines)

print("Total store value:", total_value)

print("Low stock medicines:")

for m in medicines:
    if m[3] < 10:
        print(m)