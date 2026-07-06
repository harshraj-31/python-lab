class GPS:
    def __init__(self):
        self.current = None
        self.back_stack = []
        self.forward_stack = []

    def visit(self, place):
        if self.current:
            self.back_stack.append(self.current)
        self.current = place
        self.forward_stack.clear()
        print("Current Place:", self.current)

    def back(self):
        if len(self.back_stack) == 0:
            print("No previous place")
        else:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            print("Current Place:", self.current)

    def forward(self):
        if len(self.forward_stack) == 0:
            print("No forward place")
        else:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            print("Current Place:", self.current)


# Driver Code
gps = GPS()

while True:
    print("\n1. Visit")
    print("2. Back")
    print("3. Forward")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        place = input("Enter place: ")
        gps.visit(place)

    elif choice == 2:
        gps.back()

    elif choice == 3:
        gps.forward()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
