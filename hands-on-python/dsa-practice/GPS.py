# ===========================================================
#                  GPS NAVIGATION SYSTEM
# ===========================================================
# This program simulates a simple GPS navigation system.
#
# It allows the user to:
# 1. Visit a new place.
# 2. Go back to the previous place.
# 3. Move forward to a previously visited place.
# 4. Exit the program.
#
# Two stacks are used:
# - back_stack    -> Stores previous places
# - forward_stack -> Stores places available for going forward
#
# This is an example of the STACK concept (LIFO).
# ===========================================================


class GPS:

    # -------------------------------------------------------
    # CONSTRUCTOR
    # -------------------------------------------------------
    # __init__() is automatically called when a GPS object
    # is created.

    def __init__(self):

        # Stores the current location.
        self.current = None

        # Stack for storing previous locations.
        self.back_stack = []

        # Stack for storing forward locations.
        self.forward_stack = []


    # -------------------------------------------------------
    # VISIT A NEW PLACE
    # -------------------------------------------------------
    def visit(self, place):

        # If there is already a current location,
        # save it in the back stack before moving.

        if self.current:
            self.back_stack.append(self.current)

        # Update the current location.
        self.current = place

        # When a new place is visited, the forward history
        # is cleared.

        self.forward_stack.clear()

        print("Current Place:", self.current)


    # -------------------------------------------------------
    # GO BACK
    # -------------------------------------------------------
    def back(self):

        # If there is nothing in the back stack,
        # there is nowhere to go back to.

        if len(self.back_stack) == 0:

            print("No previous place")

        else:

            # Save the current place in the forward stack
            # so that we can return to it later.

            self.forward_stack.append(self.current)

            # Remove the last place from back_stack
            # and make it the current place.

            self.current = self.back_stack.pop()

            print("Current Place:", self.current)


    # -------------------------------------------------------
    # GO FORWARD
    # -------------------------------------------------------
    def forward(self):

        # If the forward stack is empty,
        # there is no place to move forward to.

        if len(self.forward_stack) == 0:

            print("No forward place")

        else:

            # Save the current place in the back stack.

            self.back_stack.append(self.current)

            # Take the most recent place from
            # the forward stack.

            self.current = self.forward_stack.pop()

            print("Current Place:", self.current)


# ===========================================================
#                    DRIVER CODE
# ===========================================================

# Create a GPS object.
gps = GPS()


# Keep showing the menu until the user chooses Exit.

while True:

    print("\n========== GPS MENU ==========")
    print("1. Visit")
    print("2. Back")
    print("3. Forward")
    print("4. Exit")

    choice = int(input("Enter choice: "))


    # -------------------------------------------------------
    # OPTION 1: VISIT
    # -------------------------------------------------------

    if choice == 1:

        place = input("Enter place: ")
        gps.visit(place)


    # -------------------------------------------------------
    # OPTION 2: BACK
    # -------------------------------------------------------

    elif choice == 2:

        gps.back()


    # -------------------------------------------------------
    # OPTION 3: FORWARD
    # -------------------------------------------------------

    elif choice == 3:

        gps.forward()


    # -------------------------------------------------------
    # OPTION 4: EXIT
    # -------------------------------------------------------

    elif choice == 4:

        print("Program Ended")
        break


    # -------------------------------------------------------
    # INVALID OPTION
    # -------------------------------------------------------

    else:

        print("Invalid Choice")


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Stack
#    A data structure that follows LIFO:
#    Last In, First Out.
#
# ✔ append()
#    Adds an item to the end of the stack.
#
# ✔ pop()
#    Removes and returns the last item.
#
# ✔ clear()
#    Removes all items from a list.
#
# ✔ self.current
#    Stores the current location.
#
# ✔ back_stack
#    Stores previously visited locations.
#
# ✔ forward_stack
#    Stores locations that can be visited using Forward.
#
# ✔ __init__()
#    Constructor that initializes the object.
#
# ✔ visit()
#    Adds the current place to back history and
#    clears forward history.
#
# ✔ back()
#    Moves to the previous location.
#
# ✔ forward()
#    Moves to the next location in forward history.
# ===========================================================
