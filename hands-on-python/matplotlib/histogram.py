import matplotlib.pyplot as plt   # Import matplotlib library for creating graphs

# ===========================================================
#                    HISTOGRAM IN MATPLOTLIB
# ===========================================================
# A histogram is used to show the distribution of
# numerical (continuous) data.
#
# It groups data into intervals called "bins"
# and displays how many values fall into each bin.
# ===========================================================


# -----------------------------------------------------------
# SAMPLE DATA
# -----------------------------------------------------------
# This list contains numerical values that
# will be displayed in the histogram.

data = [1, 2, 2, 3, 3, 4]


# -----------------------------------------------------------
# CREATE A HISTOGRAM
# -----------------------------------------------------------
# x         -> Data to be plotted
# bins      -> Number of intervals (groups)
# color     -> Fill color of the bars
# edgecolor -> Border color of each bar

plt.hist(
    x=data,
    bins=3,
    color="lightgreen",
    edgecolor="black"
)


# -----------------------------------------------------------
# ADD TITLE
# -----------------------------------------------------------

plt.title("Simple Histogram")


# -----------------------------------------------------------
# LABEL THE X-AXIS
# -----------------------------------------------------------

plt.xlabel("Values")


# -----------------------------------------------------------
# LABEL THE Y-AXIS
# -----------------------------------------------------------

plt.ylabel("Frequency")


# -----------------------------------------------------------
# DISPLAY THE GRAPH
# -----------------------------------------------------------
# show() opens the histogram window.

plt.show()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ plt.hist()
#    Creates a histogram.
#
# ✔ x
#    Represents the numerical data.
#
# ✔ bins
#    Divides the data into equal intervals.
#
# ✔ color
#    Changes the fill color of the bars.
#
# ✔ edgecolor
#    Changes the border color of the bars.
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
#    Displays the histogram.
#
# Uses of Histogram:
# • Exam marks distribution.
# • Age distribution.
# • Temperature distribution.
# • Salary distribution.
# • Height and weight analysis.
#
# Difference Between Bar Chart and Histogram:
# • Bar Chart:
#   - Used for comparing categories.
#   - Bars have spaces between them.
#
# • Histogram:
#   - Used for continuous numerical data.
#   - Bars touch each other because the data is continuous.
# ===========================================================
