import pandas as pd   # Import pandas library for data handling

# -----------------------------------------------------------
# AGGREGATE FUNCTIONS
# -----------------------------------------------------------
# Aggregate functions are used to convert multiple values
# into a single value.
# They help in summarizing and analyzing data.

# Examples:
# mean()  -> average
# sum()   -> total
# min()   -> smallest value
# max()   -> largest value
# count() -> number of values

# -----------------------------------------------------------
# LOAD DATA FROM CSV FILE
# -----------------------------------------------------------
# Read the CSV file and store it in a DataFrame
df = pd.read_csv("pokemon.csv")

# A DataFrame is like a table (rows + columns)

# -----------------------------------------------------------
# AGGREGATE FUNCTIONS ON FULL DATAFRAME
# -----------------------------------------------------------
# numeric_only=True ensures only numeric columns are used
# (important because dataset may contain text columns)

# print(df.mean(numeric_only=True))  
# -> Finds average of all numeric columns

# print(df.sum(numeric_only=True))
# -> Finds total of all numeric columns

# print(df.min(numeric_only=True))
# -> Finds smallest value in each numeric column

# print(df.max(numeric_only=True))
# -> Finds largest value in each numeric column

# print(df.count())
# -> Counts non-empty values in each column


# -----------------------------------------------------------
# AGGREGATE FUNCTIONS ON SINGLE COLUMN
# -----------------------------------------------------------
# Here we select specific columns using df["ColumnName"]

# print(df["Height"].mean())
# -> Average height of all Pokémon

# print(df["Weight"].sum())
# -> Total weight of all Pokémon

# print(df["Height"].min())
# -> Minimum height

# print(df["Weight"].max())
# -> Maximum weight

# print(df["Name"].count())
# -> Total number of Pokémon names (non-empty rows)


# -----------------------------------------------------------
#                   GROUP BY FUNCTION (VERY IMPORTANT)
# -----------------------------------------------------------
# groupby() is used to split data into groups based on a column
# and then apply aggregate functions on each group

# Example: Group Pokémon based on their Type1
group = df.groupby("Type1")

# Now each type (Fire, Water, Grass, etc.) becomes a group
# 💭 Think:
# Now data is divided like:
# Fire group 🔥
# Water group 💧
# Grass group 🌱
# etc...


# -----------------------------------------------------------
#               APPLY AGGREGATE FUNCTIONS ON GROUPED DATA
# -----------------------------------------------------------

# print(group["Height"].mean())
# -> Average height for each Pokémon type

# print(group["Height"].sum())
# -> Total height for each type

# print(group["Height"].min())
# -> Minimum height in each type

# print(group["Height"].max())
# -> Maximum height in each type

print(group["Height"].count())
# -> Number of Pokémon in each type



# -----------------------------------------------------------
#               SUMMARY (IMPORTANT FOR EXAM)
# -----------------------------------------------------------
# 1. Aggregate functions reduce data to a single value
# 2. Can be applied on:
#    - Entire DataFrame
#    - Specific column
#    - Grouped data using groupby()
# 3. groupby() is used for category-wise analysis