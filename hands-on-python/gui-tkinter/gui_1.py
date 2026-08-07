import tkinter as tk   # Import tkinter library for creating GUI applications

# ===========================================================
#            FIRST TKINTER GUI PROGRAM
# ===========================================================
# This program creates a simple GUI window
# with a title, size, and background color.
# ===========================================================


# ===========================================================
# CREATE THE MAIN WINDOW
# ===========================================================
# Tk() creates the main application window.

window = tk.Tk()


# ===========================================================
# SET WINDOW SIZE
# ===========================================================
# geometry("width x height")
# Sets the width and height of the window.

window.geometry("420x420")


# ===========================================================
# SET WINDOW TITLE
# ===========================================================
# The title appears at the top of the window.

window.title("First GUI PROGRAM")


# ===========================================================
# CHANGE BACKGROUND COLOR
# ===========================================================
# config() changes properties of the window.
# Here, it changes the background color.

window.config(background="red")


# ===========================================================
# START THE APPLICATION
# ===========================================================
# mainloop() keeps the window open and waits
# for user interaction.

window.mainloop()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ import tkinter as tk
#    Imports the tkinter library.
#
# ✔ Tk()
#    Creates the main GUI window.
#
# ✔ geometry("420x420")
#    Sets the size of the window.
#    (Width = 420 pixels, Height = 420 pixels)
#
# ✔ title()
#    Sets the title displayed on the title bar.
#
# ✔ config()
#    Changes window properties such as
#    background color, cursor, etc.
#
# ✔ background="red"
#    Sets the background color of the window.
#
# ✔ mainloop()
#    Starts the GUI event loop and keeps
#    the window running until it is closed.
#
# Common Background Colors:
# • red
# • blue
# • green
# • yellow
# • white
# • black
# • pink
# • skyblue
#
# Uses:
# • Desktop Applications
# • Login Forms
# • Student Management Systems
# • Calculator
# • Attendance Systems
# ===========================================================
