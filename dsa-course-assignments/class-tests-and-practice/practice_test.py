# Q1: List operations

def common_elements(list1, list2):
    common = list(set(list1) & set(list2))
    print("Common elements:", common)


def difference_elements(list1, list2):
    diff = list(set(list1) - set(list2))
    print("Elements in List1 but not in List2:", diff)


# Taking input
list1 = list(map(int, input("Enter numbers for List1 separated by space: ").split()))
list2 = list(map(int, input("Enter numbers for List2 separated by space: ").split()))

common_elements(list1, list2)
difference_elements(list1, list2)

# Q2: Separate strings based on length

strings = []

for i in range(10):
    s = input(f"Enter string {i+1}: ")
    strings.append(s)

short_strings = []
long_strings = []

for s in strings:
    if len(s) <= 3:
        short_strings.append(s)
    else:
        long_strings.append(s)

print("Strings with length <= 3:", short_strings)
print("Strings with length > 3:", long_strings)

# Q3: Read list from file and sort

filename = "numbers.txt"

with open(filename, "r") as file:
    data = file.read()

numbers = list(map(int, data.split(",")))

numbers.sort()

print("Sorted list:", numbers)

# Q4: States seats program

states = {
    "MP": (29, 11),
    "UP": (80, 31),
    "TN": (39, 18),
    "MH": (48, 19),
    "GJ": (26, 11),
    "RJ": (25, 10),
    "HP": (4, 3)
}


def total_seats():
    total = 0
    for seats in states.values():
        total += seats[0] + seats[1]
    print("Total number of seats:", total)


def sort_lok_sabha():
    sorted_states = sorted(
        states.items(),
        key=lambda x: x[1][0],
        reverse=True
    )

    print("States sorted by Lok Sabha seats (descending):")
    for state, seats in sorted_states:
        print(state, seats[0])


def least_rajya_sabha():
    min_state = min(
        states.items(),
        key=lambda x: x[1][1]
    )

    print("State with least Rajya Sabha seats:")
    print(min_state[0], min_state[1][1])


# Menu
while True:

    print("\nMENU")
    print("1. Total seats")
    print("2. Sort by Lok Sabha seats")
    print("3. Least Rajya Sabha seats")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        total_seats()

    elif choice == "2":
        sort_lok_sabha()

    elif choice == "3":
        least_rajya_sabha()

    elif choice == "4":
        break

    else:
        print("Invalid choice")