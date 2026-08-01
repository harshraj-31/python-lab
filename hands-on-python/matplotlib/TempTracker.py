import matplotlib.pyplot as plt     # Import matplotlib for graphs
from tkinter import *               # Import tkinter for GUI (Graphical User Interface)

# ===========================================================
#            WEATHER DATA ANALYZER USING TKINTER
# ===========================================================
# This program allows the user to:
# 1. Add daily temperature data.
# 2. Store the data in a text file.
# 3. Analyze the stored temperatures.
# 4. Sort the temperatures.
# 5. Display a temperature graph.
# ===========================================================


# ===========================================================
#                  ADD WEATHER DATA
# ===========================================================
# Reads the date and temperature entered by the user
# and saves them into "weather.txt".

def add_data():

    # Get values entered in the Entry boxes.
    date = entry_date.get()
    temp = entry_temp.get()

    # Open the file in Append mode.
    # Existing data remains, and new data is added at the end.
    with open("weather.txt", "a") as f:
        f.write(date + "," + temp + "\n")

    # Display success message.
    result_label.config(text="Data Saved!")


# ===========================================================
#                  LOAD DATA FROM FILE
# ===========================================================
# Reads all records from weather.txt and stores them
# into two separate lists.

def load_data():

    dates = []
    temps = []

    try:
        with open("weather.txt", "r") as f:

            for line in f:

                # Remove newline and split using comma.
                d, t = line.strip().split(",")

                dates.append(d)
                temps.append(float(t))

    # If the file does not exist,
    # simply return empty lists.
    except:
        pass

    return dates, temps


# ===========================================================
#              ANALYZE TEMPERATURE DATA
# ===========================================================
# Calculates:
# - Maximum Temperature
# - Minimum Temperature
# - Average Temperature
# - Number of Hot Days (>35°C)

def analyze():

    dates, temps = load_data()

    # Check whether data exists.
    if len(temps) == 0:
        result_label.config(text="No Data Found")
        return

    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = sum(temps) / len(temps)

    # Count the number of hot days.
    hot_days = 0

    for t in temps:
        if t > 35:
            hot_days += 1

    # Display the calculated results.
    result_label.config(
        text=f"Max: {max_temp}   Min: {min_temp}   Avg: {avg_temp:.2f}   Hot Days: {hot_days}"
    )


# ===========================================================
#                  SORT TEMPERATURE DATA
# ===========================================================
# Sorts all temperatures from highest to lowest.

def sort_data():

    dates, temps = load_data()

    # Combine both lists into a single list.
    data = list(zip(dates, temps))

    # Sort using temperature values.
    data.sort(key=lambda x: x[1], reverse=True)

    text = "Sorted (High to Low):\n"

    for d, t in data:
        text += f"{d} -> {t}\n"

    result_label.config(text=text)


# ===========================================================
#                  DISPLAY LINE GRAPH
# ===========================================================
# Creates a line graph showing the temperature trend.

def graph():

    dates, temps = load_data()

    if len(temps) == 0:
        result_label.config(text="No Data Found")
        return

    # X-axis = Dates
    # Y-axis = Temperatures

    plt.plot(dates, temps, marker="o")

    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    # Rotate date labels for better readability.
    plt.xticks(rotation=45)

    plt.show()


# ===========================================================
#                 CREATE THE GUI WINDOW
# ===========================================================

# Create the main application window.
root = Tk()

# Set the title of the window.
root.title("Weather Analyzer")

# Set the window size.
root.geometry("500x300")


# ===========================================================
#                  INPUT FIELDS
# ===========================================================

Label(root, text="Date").pack()

entry_date = Entry(root)
entry_date.pack()

Label(root, text="Temperature").pack()

entry_temp = Entry(root)
entry_temp.pack()


# ===========================================================
#                  BUTTONS
# ===========================================================
# Each button is connected to a function using command=.

Button(root, text="Add Data", command=add_data).pack()

Button(root, text="Analyze", command=analyze).pack()

Button(root, text="Sort Data", command=sort_data).pack()

Button(root, text="Show Graph", command=graph).pack()


# ===========================================================
#                RESULT DISPLAY LABEL
# ===========================================================
# Used to display messages and analysis results.

result_label = Label(root, text="", fg="blue")
result_label.pack()


# ===========================================================
#                 START THE APPLICATION
# ===========================================================
# Keeps the GUI running until the user closes it.

root.mainloop()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Tk() -> Creates the main GUI window.
#
# ✔ Label() -> Displays text.
#
# ✔ Entry() -> Takes user input.
#
# ✔ Button() -> Creates a clickable button.
#
# ✔ pack() -> Arranges GUI widgets automatically.
#
# ✔ get() -> Reads data entered in an Entry widget.
#
# ✔ config() -> Updates widget properties (like Label text).
#
# ✔ with open("file","a")
#    Opens a file in Append mode.
#
# ✔ with open("file","r")
#    Opens a file in Read mode.
#
# ✔ zip()
#    Combines multiple lists into one.
#
# ✔ sort()
#    Arranges data in ascending or descending order.
#
# ✔ lambda
#    Creates a small anonymous function for sorting.
#
# ✔ plt.plot()
#    Creates a line graph.
#
# ✔ plt.xticks(rotation=45)
#    Rotates X-axis labels for better visibility.
#
# ✔ mainloop()
#    Starts the GUI event loop and keeps the window open.
# ===========================================================
