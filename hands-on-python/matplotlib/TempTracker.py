import matplotlib.pyplot as plt
from tkinter import *

# ------------------ ADD DATA ------------------
def add_data():
    date = entry_date.get()
    temp = entry_temp.get()

    with open("weather.txt", "a") as f:
        f.write(date + "," + temp + "\n")

    result_label.config(text="Data Saved!")

# ------------------ LOAD DATA ------------------
def load_data():
    dates = []
    temps = []

    try:
        with open("weather.txt", "r") as f:
            for line in f:
                d, t = line.strip().split(",")
                dates.append(d)
                temps.append(float(t))
    except:
        pass

    return dates, temps

# ------------------ ANALYSIS ------------------
def analyze():
    dates, temps = load_data()

    if len(temps) == 0:
        result_label.config(text="No Data Found")
        return

    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = sum(temps) / len(temps)

    hot_days = 0
    for t in temps:
        if t > 35:
            hot_days += 1

    result_label.config(
        text=f"Max:{max_temp}  Min:{min_temp}  Avg:{avg_temp:.2f}  Hot Days:{hot_days}"
    )

# ------------------ SORT ------------------
def sort_data():
    dates, temps = load_data()

    data = list(zip(dates, temps))
    data.sort(key=lambda x: x[1], reverse=True)

    text = "Sorted (High to Low):\n"
    for d, t in data:
        text += f"{d} -> {t}\n"

    result_label.config(text=text)

# ------------------ GRAPH ------------------
def graph():
    dates, temps = load_data()

    if len(temps) == 0:
        result_label.config(text="No Data Found")
        return

    plt.plot(dates, temps, marker="o")
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.xticks(rotation=45)
    plt.show()

# ------------------ GUI ------------------
root = Tk()
root.title("Weather Analyzer")
root.geometry("500x300")
Label(root, text="Date").pack()
entry_date = Entry(root)
entry_date.pack()

Label(root, text="Temperature").pack()
entry_temp = Entry(root)
entry_temp.pack()

Button(root, text="Add Data", command=add_data).pack()
Button(root, text="Analyze", command=analyze).pack()
Button(root, text="Sort Data", command=sort_data).pack()
Button(root, text="Show Graph", command=graph).pack()

result_label = Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()