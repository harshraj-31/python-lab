import pandas as pd   # Import the pandas library to work with tables and CSV files

# ===========================================================
#               AGGREGATE FUNCTIONS IN PANDAS
# ===========================================================
# Aggregate functions are used when we want to summarize data.
# Instead of looking at every single value, they return
# one meaningful result.
#
# Common aggregate functions:
# mean()  -> Finds the average value
# sum()   -> Adds all values together
# min()   -> Finds the smallest value
# max()   -> Finds the largest value
# count() -> Counts non-empty values
# ===========================================================


# -----------------------------------------------------------
# LOAD THE CSV FILE
# -----------------------------------------------------------
# Read the pokemon.csv file and store it inside a DataFrame.
# A DataFrame is like an Excel sheet with rows and columns.

df = pd.read_csv("pokemon.csv")


# -----------------------------------------------------------
# APPLY AGGREGATE FUNCTIONS ON THE ENTIRE DATAFRAME
# -----------------------------------------------------------
# Since the dataset contains both numbers and text,
# numeric_only=True tells pandas to ignore text columns
# and perform calculations only on numeric columns.

# print(df.mean(numeric_only=True))
# Finds the average of every numeric column.

# print(df.sum(numeric_only=True))
# Adds all values in every numeric column.

# print(df.min(numeric_only=True))
# Displays the smallest value from every numeric column.

# print(df.max(numeric_only=True))
# Displays the largest value from every numeric column.

# print(df.count())
# Counts how many non-empty values are present in each column.


# -----------------------------------------------------------
# APPLY AGGREGATE FUNCTIONS ON A SINGLE COLUMN
# -----------------------------------------------------------
# If we need information about only one column,
# we select it using:
# df["ColumnName"]

# print(df["Height"].mean())
# Calculates the average height of all Pokémon.

# print(df["Weight"].sum())
# Calculates the total weight of all Pokémon.

# print(df["Height"].min())
# Finds the shortest Pokémon.

# print(df["Weight"].max())
# Finds the heaviest Pokémon.

# print(df["Name"].count())
# Counts how many Pokémon names are available.


# ===========================================================
#                   GROUP BY FUNCTION
# ===========================================================
# groupby() is one of the most useful functions in pandas.
#
# It divides the data into separate groups based on
# the values of a particular column.
#
# Here we are grouping Pokémon according to their Type1.
#
# Example:
# Fire   -> All Fire Pokémon
# Water  -> All Water Pokémon
# Grass  -> All Grass Pokémon
# Electric -> All Electric Pokémon
#
# Once the groups are created, we can perform calculations
# on each group separately.

group = df.groupby("Type1")


# -----------------------------------------------------------
# APPLY AGGREGATE FUNCTIONS ON GROUPED DATA
# -----------------------------------------------------------
# Now each Pokémon type is treated as its own group.

# print(group["Height"].mean())
# Finds the average height of Pokémon in each type.

# print(group["Height"].sum())
# Adds the heights of Pokémon belonging to each type.

# print(group["Height"].min())
# Finds the shortest Pokémon in every type.

# print(group["Height"].max())
# Finds the tallest Pokémon in every type.

print(group["Height"].count())
# Counts how many Pokémon belong to each type.


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Aggregate functions are used to summarize data.
#
# ✔ They can be applied on:
#    1. The entire DataFrame
#    2. A specific column
#    3. Grouped data using groupby()
#
# ✔ groupby() divides the dataset into categories
#    so calculations can be performed on each category separately.
#
# Example:
# Instead of finding the average height of all Pokémon,
# groupby("Type1") lets us find:
#
# Fire     -> Average Height
# Water    -> Average Height
# Grass    -> Average Height
# Electric -> Average Height
#
# This makes category-wise analysis very easy.
# ===========================================================
