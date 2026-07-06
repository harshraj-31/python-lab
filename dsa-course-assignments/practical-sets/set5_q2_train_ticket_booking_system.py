# SET-5 Q2: Train Ticket Booking System

passengers = []

# Input details of 5 passengers
for i in range(5):

    pid = input("Passenger ID: ")
    name = input("Passenger Name: ")
    train = input("Train Number: ")
    source = input("Source Station: ")
    dest = input("Destination Station: ")
    fare = float(input("Ticket Fare: "))
    seats = int(input("Number of Seats: "))

    passengers.append(
        [pid, name, train, source, dest, fare, seats]
    )


# Store data in file
file = open("Train_booking.txt", "w")

for p in passengers:
    file.write(str(p) + "\n")

file.close()

print("\nData saved to Train_booking.txt")


# 1. Display bookings for specific train number

train_input = input(
    "\nEnter train number to search: "
)

print("\nBookings for train:", train_input)

for p in passengers:
    if p[2] == train_input:
        print(p)


# 2. Count total seats booked for each train

seat_count = {}

for p in passengers:

    train = p[2]

    if train in seat_count:
        seat_count[train] += p[6]
    else:
        seat_count[train] = p[6]

print("\nTotal seats booked per train:")
print(seat_count)


# 3. Calculate total fare collected for each train

fare_total = {}

for p in passengers:

    train = p[2]
    total_fare = p[5] * p[6]

    if train in fare_total:
        fare_total[train] += total_fare
    else:
        fare_total[train] = total_fare

print("\nTotal fare collected per train:")
print(fare_total)


# 4. Count trains from source to destination

src = input("\nEnter source station: ")
dst = input("Enter destination station: ")

count = 0

for p in passengers:
    if p[3] == src and p[4] == dst:
        count += 1

print(
    "\nNumber of trains from",
    src,
    "to",
    dst,
    ":",
    count
)