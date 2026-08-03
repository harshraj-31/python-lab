import matplotlib.pyplot as plt   # Import matplotlib library for creating graphs

# ===========================================================
#                    PIE CHART IN MATPLOTLIB
# ===========================================================
# A Pie Chart is a circular graph divided into slices.
# Each slice represents the percentage of the total.
#
# It is mainly used to show how a whole is divided
# among different categories.
# ===========================================================


# -----------------------------------------------------------
# STORE CATEGORY NAMES
# -----------------------------------------------------------
# These labels will be displayed on each slice.

categories = [
    "Freshmen",
    "Sophomores",
    "Juniors",
    "Seniors"
]


# -----------------------------------------------------------
# STORE VALUES
# -----------------------------------------------------------
# These values represent the number of students
# in each category.

values = [300, 250, 274, 221]


# -----------------------------------------------------------
# DEFINE SLICE COLORS
# -----------------------------------------------------------
# Each slice of the pie chart will have
# a different color.

colors = ["red", "yellow", "darkblue", "green"]


# -----------------------------------------------------------
# CREATE THE PIE CHART
# -----------------------------------------------------------
# values      -> Size of each slice
# labels      -> Name of each category
# autopct     -> Displays percentage on each slice
# colors      -> Sets slice colors
# explode     -> Separates selected slices from the pie

plt.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    colors=colors,
    explode=[0, 0.1, 0, 0.1]
)


# -----------------------------------------------------------
# DISPLAY THE PIE CHART
# -----------------------------------------------------------
# show() opens the graph window.

plt.show()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ plt.pie()
#    Creates a pie chart.
#
# ✔ values
#    Determines the size of each slice.
#
# ✔ labels
#    Displays category names on the chart.
#
# ✔ colors
#    Assigns different colors to each slice.
#
# ✔ autopct="%1.1f%%"
#    Displays percentage values.
#
#    %1.1f means:
#       1 -> Minimum width
#       .1 -> One digit after the decimal
#       f -> Floating-point number
#       %% -> Displays the % symbol
#
# ✔ explode
#    Moves selected slices slightly away
#    from the center to highlight them.
#
# ✔ plt.show()
#    Displays the chart.
#
# Uses of Pie Chart:
# • Student distribution by class.
# • Market share of companies.
# • Budget allocation.
# • Population distribution.
# • Product sales percentage.
# ===========================================================
