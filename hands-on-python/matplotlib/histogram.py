import matplotlib.pyplot as plt

# histogram = A visual representation of the distribution of the quantitative data
#             They group values into bins (intervals)
#             and counts how many fall in each range



# simple data
data = [1, 2, 2, 3, 3, 4]

# histogram
plt.hist(x=data,
        bins=3, 
        color="lightgreen",
        edgecolor="black")

# labels
plt.title("Simple Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

# show
plt.show()