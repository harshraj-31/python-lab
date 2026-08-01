import matplotlib.pyplot as plt   # Import matplotlib library for creating graphs

# ===========================================================
#        WEEKLY FITNESS / STEP TRACKER APPLICATION
# ===========================================================
# This program allows the user to:
# 1. Add weekly step data.
# 2. Calculate total, highest and lowest activity.
# 3. Display a line graph.
# 4. Save the data into a text file.
# ===========================================================


# Dictionary to store user data.
# Format:
# {
#     "Karan": [2000,3000,4000,5000,6000,7000,8000],
#     "Anas" : [1000,2000,3000,4000,5000,6000,7000]
# }

users = {}


# ===========================================================
#                ADD USER DETAILS
# ===========================================================
# This function asks the user to enter:
# - User name
# - Steps for 7 days
# The data is then stored in the dictionary.

def add_user():

    name = input("Enter user name: ")

    steps = []

    # Take step count for all 7 days.
    for i in range(1, 8):
        step = int(input(f"Enter Day {i} steps: "))
        steps.append(step)

    # Store the list of steps using the user's name as the key.
    users[name] = steps


# ===========================================================
#            CALCULATE FITNESS STATISTICS
# ===========================================================
# This function calculates:
# - Total weekly steps
# - Highest activity day
# - Lowest activity day
# - Average steps for each day across all users

def calculate():

    # Process every user one by one.
    for name, steps in users.items():

        total_steps = sum(steps)
        max_steps = max(steps)
        min_steps = min(steps)

        # index() returns the position of the value.
        # +1 converts it into Day Number (1-7).

        high_activity_day = steps.index(max_steps) + 1
        low_activity_day = steps.index(min_steps) + 1

        print(f"\n{name} SUMMARY")
        print("Total Steps:", total_steps)
        print("Highest Activity Day:", high_activity_day, "(", max_steps, ")")
        print("Lowest Activity Day:", low_activity_day, "(", min_steps, ")")

    # -------------------------------------------------------
    # Calculate average steps for each day.
    # Example:
    # Day 1 Average = (User1 + User2 + User3) / Total Users
    # -------------------------------------------------------

    print("\nAverage Steps Per Day")

    for i in range(7):

        total = 0

        for user in users:
            total += users[user][i]

        print(f"Day {i+1}: {total / len(users)}")


# ===========================================================
#                 DISPLAY LINE GRAPH
# ===========================================================
# Draws a line graph showing the step count
# of every user over 7 days.

def plot_graph():

    for name, steps in users.items():

        # X-axis = Days (1 to 7)
        # Y-axis = Number of steps
        # label = User name (shown in legend)

        plt.plot(range(1, 8), steps, label=name)

    plt.xlabel("Days")
    plt.ylabel("Steps")
    plt.title("Weekly Activity Report")

    # Shows which line belongs to which user.
    plt.legend()

    # Save the graph as an image.
    plt.savefig("activity.png")

    # Display the graph.
    plt.show()


# ===========================================================
#                 SAVE DATA TO FILE
# ===========================================================
# Stores all user data in a text file.
# If the file already exists, it is overwritten.

def save_data():

    with open("data.txt", "w") as f:

        for name, steps in users.items():

            f.write(name + ":\n")

            for s in steps:
                f.write(str(s) + " ")

            f.write("\n")


# ===========================================================
#                   MAIN MENU
# ===========================================================
# Continuously displays the menu until
# the user chooses Exit.

while True:

    print("\n========== MENU ==========")
    print("1. Add User")
    print("2. Calculate Statistics")
    print("3. Plot Graph")
    print("4. Save Data")
    print("0. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_user()

    elif ch == 2:
        calculate()

    elif ch == 3:
        plot_graph()

    elif ch == 4:
        save_data()

    elif ch == 0:
        print("Program Ended...")
        break

    else:
        print("Invalid Choice! Please try again.")


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Dictionary stores user names and their weekly steps.
#
# ✔ List stores the step count for 7 days.
#
# ✔ sum() -> Calculates total steps.
#
# ✔ max() -> Finds the highest step count.
#
# ✔ min() -> Finds the lowest step count.
#
# ✔ index() -> Returns the position of a value.
#
# ✔ plt.plot() -> Creates a line graph.
#
# ✔ plt.legend() -> Displays user names on the graph.
#
# ✔ plt.savefig() -> Saves the graph as an image file.
#
# ✔ with open("file.txt","w")
#    Opens a file in write mode and automatically closes it.
#
# ✔ while True
#    Keeps the menu running until the user selects Exit.
# ===========================================================
