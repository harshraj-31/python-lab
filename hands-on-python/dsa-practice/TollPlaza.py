class TollPlaza:
    def __init__(self):
        self.queue = ["Empty"] * 5
        self.front = 0
        self.rear = -1
        self.count = 0

    def enter(self, vehicle):
        if self.count == 5:
            print("Toll Plaza is Full")
        else:
            self.rear = (self.rear + 1) % 5
            self.queue[self.rear] = vehicle
            self.count += 1
            print(vehicle, "entered")

    def exit(self):
        if self.count == 0:
            print("Toll Plaza is Empty")
        else:
            print(self.queue[self.front], "left")
            self.queue[self.front] = "Empty"
            self.front = (self.front + 1) % 5
            self.count -= 1

    def display(self):
        print(self.queue)


# Driver Code
toll = TollPlaza()

while True:
    print("\n1. Vehicle Enter")
    print("2. Vehicle Exit")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        vehicle = input("Enter vehicle name: ")
        toll.enter(vehicle)

    elif choice == 2:
        toll.exit()

    elif choice == 3:
        toll.display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
