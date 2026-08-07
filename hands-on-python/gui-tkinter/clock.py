import tkinter as tk          # Import tkinter for GUI
from time import *            # Import all functions from the time module

# ===========================================================
#                DIGITAL CLOCK USING TKINTER
# ===========================================================
# This program displays:
# 1. Current Time
# 2. Current Day
# 3. Current Date
#
# The clock updates automatically every second.
# ===========================================================


# ===========================================================
#               UPDATE CLOCK
# ===========================================================
# This function gets the current time, day, and date
# and updates the labels every second.

def update():

    # Get current time.
    # %I -> Hour (12-hour format)
    # %M -> Minutes
    # %S -> Seconds
    # %p -> AM / PM
    time_string = strftime("%I:%M:%S %p")

    # Display time.
    timelabel.config(text=time_string)

    # Get current day.
    # %A -> Full weekday name.
    day_string = strftime("%A")

    # Display day.
    daylabel.config(text=day_string)

    # Get current date.
    # %B -> Month name
    # %d -> Day of month
    # %Y -> Year
    date_string = strftime("%B %d, %Y")

    # Display date.
    datelabel.config(text=date_string)

    # Call update() again after 1000 milliseconds (1 second).
    timelabel.after(1000, update)


# ===========================================================
#               CREATE MAIN WINDOW
# ===========================================================

m = tk.Tk()

# Set window size.
m.geometry("500x500")

# Set window title.
m.title("Clock")

# Set background color.
m.config(background="black")


# ===========================================================
#               TIME LABEL
# ===========================================================
# Displays the current time.

timelabel = tk.Label(
    m,
    font=("Arial", 50),
    fg="green",
    bg="black"
)

timelabel.place(x=80, y=100)


# ===========================================================
#               DAY LABEL
# ===========================================================
# Displays the current day.

daylabel = tk.Label(
    m,
    font=("Ink Free", 25),
    fg="red",
    bg="white"
)

daylabel.place(x=150, y=210)


# ===========================================================
#               DATE LABEL
# ===========================================================
# Displays the current date.

datelabel = tk.Label(
    m,
    font=("Ink Free", 25),
    fg="blue",
    bg="white"
)

datelabel.place(x=100, y=320)


# ===========================================================
#               START CLOCK
# ===========================================================
# Call update() once to start the clock.

update()


# ===========================================================
#               START GUI
# ===========================================================
# Keeps the application running.

m.mainloop()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Tk()
#    Creates the main GUI window.
#
# ✔ Label()
#    Displays text on the window.
#
# ✔ config()
#    Changes widget properties such as text.
#
# ✔ strftime()
#    Returns the current date or time in a specified format.
#
# Common Format Codes:
# %I -> Hour (12-hour format)
# %H -> Hour (24-hour format)
# %M -> Minutes
# %S -> Seconds
# %p -> AM / PM
# %A -> Full day name
# %B -> Full month name
# %d -> Day of month
# %Y -> Year
#
# ✔ after(1000, update)
#    Calls update() again after 1000 milliseconds (1 second),
#    making the clock refresh continuously.
#
# ✔ place()
#    Positions widgets using X and Y coordinates.
#
# ✔ mainloop()
#    Starts the GUI event loop and keeps the window open.
#
# Uses:
# • Digital Clock
# • Date & Time Display
# • Dashboard Applications
# • Attendance Systems
# ===========================================================
