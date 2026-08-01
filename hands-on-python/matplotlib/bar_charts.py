import matplotlib.pyplot as plt   # Import matplotlib library for creating graphs

# ===========================================================
#                    BAR CHART IN MATPLOTLIB
# ===========================================================
# A bar chart is used to compare different categories of data.
# The height of each bar represents the value of that category.
# ===========================================================


# -----------------------------------------------------------
# STORE CATEGORY NAMES
# -----------------------------------------------------------
# These values will be displayed on the X-axis.

categories = [
    "Grains",
    "Fruit",
    "Vegetables",
    "Protein",
    "Dairy",
    "Sweets"
]


# -----------------------------------------------------------
# STORE VALUES
# -----------------------------------------------------------
# These values represent the quantity consumed
# for each food category.

values = [4, 3, 5, 5, 4, 1]


# -----------------------------------------------------------
# CREATE A BAR CHART
# -----------------------------------------------------------
# Syntax:
# plt.bar(x_values, y_values)
#
# categories -> X-axis labels
# values     -> Height of each bar
# color      -> Color of the bars

plt.bar(categories, values, color="red")


# -----------------------------------------------------------
# HORIZONTAL BAR CHART
# -----------------------------------------------------------
# Use barh() instead of bar() to create
# a horizontal bar chart.

# plt.barh(categories, values, color="skyblue")


# -----------------------------------------------------------
# ADD TITLE AND AXIS LABELS
# -----------------------------------------------------------

plt.title("Daily Food Consumption")

# Label for X-axis
plt.xlabel("Food Category")

# Label for Y-axis
plt.ylabel("Quantity")


# -----------------------------------------------------------
# DISPLAY THE GRAPH
# -----------------------------------------------------------
# show() opens the graph window.

plt.show()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ plt.bar()
#    Creates a vertical bar chart.
#
# ✔ plt.barh()
#    Creates a horizontal bar chart.
#
# ✔ categories
#    Displayed on the X-axis.
#
# ✔ values
#    Determine the height (or length) of each bar.
#
# ✔ color
#    Changes the color of the bars.
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
# Uses of Bar Chart:
# • Compare sales of products.
# • Compare marks of students.
# • Compare monthly expenses.
# • Compare quantities of different categories.
# ===========================================================
