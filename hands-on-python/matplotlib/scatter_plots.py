import matplotlib.pyplot as plt   # Import matplotlib library for creating graphs

# ===========================================================
#                 SCATTER PLOT IN MATPLOTLIB
# ===========================================================
# A Scatter Plot is used to show the relationship
# between two numerical variables.
#
# It helps us identify whether there is:
# ✔ Positive Correlation
# ✔ Negative Correlation
# ✔ No Correlation
#
# Example:
# Hours Studied vs. Test Scores
# ===========================================================


# -----------------------------------------------------------
# X-AXIS DATA
# -----------------------------------------------------------
# Represents the number of hours studied.

x1 = [0, 1, 1, 2, 4, 5, 6, 7, 8]


# -----------------------------------------------------------
# Y-AXIS DATA
# -----------------------------------------------------------
# Represents the grades obtained by students.

y1 = [55, 60, 65, 62, 70, 75, 78, 85, 87]


# -----------------------------------------------------------
# SECOND DATASET (OPTIONAL)
# -----------------------------------------------------------
# Another class can also be plotted on the
# same graph for comparison.

# x2 = [0, 1, 1, 2, 4, 8, 6, 7, 8]
# y2 = [50, 65, 87, 42, 88, 76, 74, 87, 77]


# -----------------------------------------------------------
# CREATE A SCATTER PLOT
# -----------------------------------------------------------
# x1, y1   -> X and Y coordinates
# color    -> Color of the points
# s         -> Size of each point
# alpha    -> Transparency (0 = invisible, 1 = fully visible)
# label    -> Name displayed in the legend

plt.scatter(
    x1,
    y1,
    color="red",
    s=200,
    alpha=0.5,
    label="Class A"
)


# -----------------------------------------------------------
# ADD SECOND DATASET (OPTIONAL)
# -----------------------------------------------------------
# Uncomment this section to compare another class.

# plt.scatter(
#     x2,
#     y2,
#     color="skyblue",
#     s=200,
#     alpha=0.8,
#     label="Class B"
# )


# -----------------------------------------------------------
# ADD TITLE
# -----------------------------------------------------------

plt.title("Test Scores")


# -----------------------------------------------------------
# LABEL THE X-AXIS
# -----------------------------------------------------------

plt.xlabel("Hours Studied")


# -----------------------------------------------------------
# LABEL THE Y-AXIS
# -----------------------------------------------------------

plt.ylabel("Grade")


# -----------------------------------------------------------
# DISPLAY LEGEND
# -----------------------------------------------------------
# Shows the labels of different datasets.

plt.legend()


# -----------------------------------------------------------
# DISPLAY THE GRAPH
# -----------------------------------------------------------

plt.show()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ plt.scatter()
#    Creates a scatter plot.
#
# ✔ x values
#    Represent the independent variable.
#
# ✔ y values
#    Represent the dependent variable.
#
# ✔ color
#    Changes the color of the points.
#
# ✔ s
#    Changes the size of the points.
#
# ✔ alpha
#    Controls the transparency of the points.
#    0   -> Completely transparent
#    1   -> Fully visible
#
# ✔ label
#    Assigns a name to the dataset.
#
# ✔ plt.legend()
#    Displays the labels of different datasets.
#
# ✔ plt.show()
#    Displays the graph.
#
# Correlation:
# • Positive Correlation (+)
#   As X increases, Y also increases.
#
# • Negative Correlation (-)
#   As X increases, Y decreases.
#
# • No Correlation
#   No clear relationship between X and Y.
#
# Uses of Scatter Plot:
# • Study hours vs. Marks
# • Height vs. Weight
# • Advertisement Cost vs. Sales
# • Temperature vs. Ice Cream Sales
# • Experience vs. Salary
# ===========================================================
