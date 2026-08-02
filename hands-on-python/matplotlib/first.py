import matplotlib.pyplot as plt   # Import matplotlib library for creating graphs

# ===========================================================
#                 LINE PLOT CUSTOMIZATION
# ===========================================================
# A line plot is used to show trends or changes over time.
# Here, we are displaying the number of students
# in different years.
# ===========================================================


# -----------------------------------------------------------
# X-AXIS DATA
# -----------------------------------------------------------
# These values represent the years.

x = [2023, 2024, 2025, 2026]


# -----------------------------------------------------------
# Y-AXIS DATA
# -----------------------------------------------------------
# These values represent the number of students.

y = [15, 25, 30, 20]


# -----------------------------------------------------------
# CREATE A LINE PLOT
# -----------------------------------------------------------
# plot(x, y) draws a line graph.
#
# marker="."
#     Displays a dot at each data point.
#
# markersize=20
#     Increases the size of the marker.
#
# markerfacecolor="red"
#     Changes the color of the marker.
#
# linestyle="dotted"
#     Makes the line dotted instead of solid.

plt.plot(
    x,
    y,
    marker=".",
    markersize=20,
    markerfacecolor="red",
    linestyle="dotted"
)


# -----------------------------------------------------------
# ADD GRID
# -----------------------------------------------------------
# Displays horizontal and vertical grid lines,
# making the graph easier to read.

plt.grid()


# -----------------------------------------------------------
# ADD TITLE
# -----------------------------------------------------------
# fontsize changes the size of the title.
# color changes the title color.

plt.title("Class Size", fontsize=15, color="red")


# -----------------------------------------------------------
# LABEL THE X-AXIS
# -----------------------------------------------------------

plt.xlabel("Year", fontsize=10, color="darkblue")


# -----------------------------------------------------------
# LABEL THE Y-AXIS
# -----------------------------------------------------------

plt.ylabel("Students", fontsize=10, color="darkblue")


# -----------------------------------------------------------
# DISPLAY THE GRAPH
# -----------------------------------------------------------
# show() opens the graph window.

plt.show()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ plt.plot(x, y)
#    Creates a line graph.
#
# ✔ marker
#    Displays symbols at each data point.
#
# ✔ markersize
#    Changes the size of the marker.
#
# ✔ markerfacecolor
#    Changes the color of the marker.
#
# ✔ linestyle
#    Changes the style of the line.
#    Examples:
#       "-"   -> Solid
#       "--"  -> Dashed
#       ":"   -> Dotted
#       "-."  -> Dash-dot
#
# ✔ plt.grid()
#    Displays grid lines for better readability.
#
# ✔ plt.title()
#    Adds a title to the graph.
#
# ✔ plt.xlabel()
#    Adds a label to the X-axis.
#
# ✔ plt.ylabel()
#    Adds a label to the Y-axis.
#
# ✔ plt.show()
#    Displays the graph on the screen.
#
# Uses of Line Graph:
# • Population growth over years.
# • Student attendance trends.
# • Monthly sales.
# • Temperature changes.
# • Stock market analysis.
# ===========================================================
