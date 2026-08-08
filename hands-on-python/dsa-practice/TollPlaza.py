# ===========================================================
#                 TOLL PLAZA QUEUE SYSTEM
# ===========================================================
# This program simulates vehicles waiting at a toll plaza.
#
# It uses a QUEUE data structure with a fixed size of 5.
#
# Queue follows FIFO:
# First In, First Out
#
# Operations:
# 1. Vehicle Enter -> Enqueue
# 2. Vehicle Exit  -> Dequeue
# 3. Display Queue
# 4. Exit Program
# ===========================================================


class TollPlaza:

    # -------------------------------------------------------
    # CONSTRUCTOR
    # -------------------------------------------------------
    # Initializes the queue and its required variables.

    def __init__(self):

        # Create a queue with 5 empty positions.
        self.queue = ["Empty"] * 5

        # front points to the first vehicle in the queue.
        self.front = 0

        # rear points to the last vehicle.
        # Initially, there is no vehicle.
        self.rear = -1

        # Keeps track of how many vehicles are currently
        # present in the queue.
        self.count = 0


    # -------------------------------------------------------
    # VEHICLE ENTER - ENQUEUE
    # -------------------------------------------------------
    def enter(self, vehicle):

        # If count is 5, the queue is completely full.
        if self.count == 5:

            print("Toll Plaza is Full")

        else:

            # Move rear to the next position.
            #
            # % 5 makes the queue circular.
            # Example:
            # 0 -> 1 -> 2 -> 3 -> 4 -> 0

            self.rear = (self.rear + 1) % 5

            # Store the vehicle at the rear position.
            self.queue[self.rear] = vehicle

            # Increase the number of vehicles.
            self.count += 1

            print(vehicle, "entered")


    # -------------------------------------------------------
    # VEHICLE EXIT - DEQUEUE
    # -------------------------------------------------------
    def exit(self):

        # If there are no vehicles, the queue is empty.
        if self.count == 0:

            print("Toll Plaza is Empty")

        else:

            # The vehicle at the front leaves first.
            print(self.queue[self.front], "left")

            # Mark the position as empty.
            self.queue[self.front] = "Empty"

            # Move front to the next position.
            # % 5 makes the queue circular.

            self.front = (self.front + 1) % 5

            # Decrease the number of vehicles.
            self.count -= 1


    # -------------------------------------------------------
    # DISPLAY QUEUE
    # -------------------------------------------------------
    def display(self):

        # Display the complete queue.
        print(self.queue)


# ===========================================================
#                    DRIVER CODE
# ===========================================================

# Create a TollPlaza object.
toll = TollPlaza()


# Keep displaying the menu until the user exits.

while True:

    print("\n========== TOLL PLAZA ==========")
    print("1. Vehicle Enter")
    print("2. Vehicle Exit")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))


    # -------------------------------------------------------
    # OPTION 1: VEHICLE ENTER
    # -------------------------------------------------------

    if choice == 1:

        vehicle = input("Enter vehicle name: ")
        toll.enter(vehicle)


    # -------------------------------------------------------
    # OPTION 2: VEHICLE EXIT
    # -------------------------------------------------------

    elif choice == 2:

        toll.exit()


    # -------------------------------------------------------
    # OPTION 3: DISPLAY
    # -------------------------------------------------------

    elif choice == 3:

        toll.display()


    # -------------------------------------------------------
    # OPTION 4: EXIT
    # -------------------------------------------------------

    elif choice == 4:

        print("Program Ended")
        break


    # -------------------------------------------------------
    # INVALID CHOICE
    # -------------------------------------------------------

    else:

        print("Invalid Choice")


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Queue
#    A linear data structure that follows FIFO.
#
#    FIFO = First In, First Out
#
# ✔ Enqueue
#    Adding an element to the rear of the queue.
#
# ✔ Dequeue
#    Removing an element from the front of the queue.
#
# ✔ front
#    Points to the first element.
#
# ✔ rear
#    Points to the last element.
#
# ✔ count
#    Keeps track of the number of vehicles.
#
# ✔ % 5
#    Makes the queue circular.
#
#    Example:
#    0 -> 1 -> 2 -> 3 -> 4 -> 0
#
# ✔ is Full
#    count == 5
#
# ✔ is Empty
#    count == 0
#
# ✔ append() and pop() are NOT used here.
#    The queue is implemented using an array/list
#    with front and rear pointers.
# ===========================================================
