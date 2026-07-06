class ConveyorBelt:
    def __init__(self):
        self.belt = ["Empty"] * 8

    def update(self, slot, product):
        self.belt[slot] = product
        print("Product updated!")

    def check(self, slot):
        print("Slot", slot, "contains:", self.belt[slot])

    def find(self, product):
        if product in self.belt:
            print(product, "found at slot", self.belt.index(product))
        else:
            print("Product not found")

    def full(self):
        if "Empty" in self.belt:
            print("Conveyor Belt is Not Full")
        else:
            print("Conveyor Belt is Full")

    def display(self):
        print(self.belt)


# Driver Code
belt = ConveyorBelt()

while True:
    print("\n1. Update Slot")
    print("2. Check Slot")
    print("3. Find Product")
    print("4. Check if Belt is Full")
    print("5. Display Belt")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        slot = int(input("Enter slot number (0-7): "))
        product = input("Enter product name: ")
        belt.update(slot, product)

    elif choice == 2:
        slot = int(input("Enter slot number (0-7): "))
        belt.check(slot)

    elif choice == 3:
        product = input("Enter product name: ")
        belt.find(product)

    elif choice == 4:
        belt.full()

    elif choice == 5:
        belt.display()

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
