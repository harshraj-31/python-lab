import pandas as pd   # Import pandas library

# ===========================================================
#                     PANDAS SERIES
# ===========================================================
# A Series is a one-dimensional data structure in pandas.
# It stores a single column of data along with an index.
#
# Think of it as one column from an Excel spreadsheet.
# ===========================================================


# -----------------------------------------------------------
# CREATE A SERIES FROM A LIST
# -----------------------------------------------------------
# A Python list is converted into a pandas Series.
# If no index is provided, pandas automatically
# assigns indexes starting from 0.

data = [100, 102, 104, 200, 202]

# Create the Series
# You can also provide your own custom indexes if needed.

series = pd.Series(data)   # index=["a","b","c","d","e"]

# Display the complete Series
# print(series)


# -----------------------------------------------------------
# ACCESS VALUES USING loc[]
# -----------------------------------------------------------
# loc[] is used to access data using index labels.
# (Works when custom indexes are assigned.)

# print(series.loc["a"])
# Displays the value stored at index "a".

# print(series.loc["b"])
# Displays the value stored at index "b".


# -----------------------------------------------------------
# UPDATE A VALUE
# -----------------------------------------------------------
# We can change the value stored at a particular index.

# series.loc["c"] = 74


# -----------------------------------------------------------
# ACCESS VALUES USING iloc[]
# -----------------------------------------------------------
# iloc[] is used to access data using
# integer positions (0, 1, 2, ...).

# print(series.iloc[0])
# Displays the first value in the Series.


# -----------------------------------------------------------
# FILTERING
# -----------------------------------------------------------
# Filtering returns only those values
# that satisfy a given condition.

# print(series[series >= 200])
# Displays values greater than or equal to 200.

# print(series[series < 200])
# Displays values less than 200.


# ===========================================================
#           CREATE A SERIES FROM A DICTIONARY
# ===========================================================
# When a dictionary is converted into a Series:
# - Dictionary keys become the index.
# - Dictionary values become the data.

calories = {
    "Day 1": 1750,
    "Day 2": 2000,
    "Day 3": 1700
}

series2 = pd.Series(calories)


# -----------------------------------------------------------
# ACCESS DATA
# -----------------------------------------------------------
# iloc[] accesses data using integer position.

print(series2.iloc[1])

# loc[] accesses data using the index label.

# print(series2.loc["Day 1"])
# print(series2.loc["Day 2"])


# -----------------------------------------------------------
# UPDATE A VALUE
# -----------------------------------------------------------
# Increase Day 3 calories by 500.

# series2.loc["Day 3"] += 500

# print(series2.loc["Day 3"])


# -----------------------------------------------------------
# FILTERING
# -----------------------------------------------------------
# Display values based on conditions.

# print(series2[series2 >= 2000])
# Shows days where calories are 2000 or more.

# print(series2[series2 < 2000])
# Shows days where calories are less than 2000.


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Series is a one-dimensional data structure.
#
# ✔ A Series can be created from:
#    - List
#    - Tuple
#    - Dictionary
#    - NumPy Array
#
# ✔ If no index is given, pandas creates
#    default indexes (0, 1, 2, ...).
#
# ✔ loc[]
#    Accesses values using index labels.
#
# ✔ iloc[]
#    Accesses values using integer positions.
#
# ✔ Values can be updated using:
#    series.loc["index"] = new_value
#
# ✔ Filtering Syntax:
#    series[condition]
#
# Example:
#    series[series >= 200]
#    Returns all values greater than or equal to 200.
# ===========================================================
