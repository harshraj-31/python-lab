import matplotlib.pyplot as plt

users = {}

#user data
def add_user():
    name = input("Enter user name: ")
    steps = []
    for i in range(1,8):
        step = int(input(f"Enter Day {i} steps: "))
        steps.append(step)
    users[name] = steps


def calculate():
    for name,steps in users.items():
        total_steps = sum(steps)
        max_steps = max(steps)
        min_steps = min(steps)
        high_activity_day = steps.index(max_steps) + 1
        low_activity_day  = steps.index(min_steps) + 1

        print(f"{name} SUMMARY")
        print("Total steps: ",total_steps)
        print("Highest Activity Day: ",high_activity_day,"(",max_steps,")")
        print("Lowest Activity Day:",low_activity_day,"(",min_steps,")")

        #Average steps per day(all users)
    for i in range(7):
         total = 0
         for user in users:
             total += users[user][i]
         print(f"Day {i+1} Average",total/len(users))


def plot_graph():

    for name,steps in users.items():
        #range(1,8) means [1,2,3,4,5,6,7] as X axis
        #and steps are y axis [2000,3000,5000, etc]
        #label=name ust a name for the line for the line
        #So legend shows: user names

        plt.plot(range(1,8) ,steps,label=name)

    plt.xlabel("Days")
    plt.ylabel("Steps")
    plt.title("Weekly Activity")
    plt.legend()
    plt.savefig(f"activity.png") #save image
    plt.show()

def save_data():
    with open("data.txt","w") as f:
        for name,steps in users.items():
            f.write(name+":\n")
            for s in steps:
                f.write(str(s)+" ")
            f.write("\n")

while True:
    print("1.Add user")
    print("2.Calculate")
    print("3.Plot Graph")
    print("4.Save Data")
    print("0.exit")
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
        break