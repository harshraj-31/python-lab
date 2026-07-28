import pandas as pd   # Import pandas library for working with tables and datasets

# ===========================================================
#                 DATAFRAME IN PANDAS
# ===========================================================
# A DataFrame is a 2-dimensional data structure.
# It stores data in rows and columns, just like an Excel sheet.
# Each column can contain a different type of data.
# ===========================================================


# -----------------------------------------------------------
# CREATE DATA USING A PYTHON DICTIONARY
# -----------------------------------------------------------
# Here, each key becomes a column name,
# and the list becomes the values of that column.

data = {
    "Name": ["Karan", "Anas", "Harry"],
    "Age": [22, 21, 20]
}

# Create a DataFrame from the dictionary.
# We are also assigning custom row labels (indexes).

df = pd.DataFrame(data, index=["Emp1", "Emp2", "Emp3"])

# Display the complete DataFrame
# print(df)


# -----------------------------------------------------------
# ACCESS ROWS USING loc[]
# -----------------------------------------------------------
# loc[] is used when we want to search using
# the row label (index name).

# print(df.loc["Emp3"])
# Displays the row with index "Emp3"

# print(df.loc["Emp2"])
# Displays the row with index "Emp2"


# -----------------------------------------------------------
# ACCESS ROWS USING iloc[]
# -----------------------------------------------------------
# iloc[] is used when we want to access rows
# using their numerical position (starting from 0).

# print(df.iloc[0])
# Displays the first row

# print(df.iloc[1])
# Displays the second row


# -----------------------------------------------------------
# ADD A NEW COLUMN
# -----------------------------------------------------------
# A new column can be added by simply assigning
# a list of values to a new column name.

df["Job"] = ["CEO", "N/A", "Cashier"]

# Display the DataFrame after adding the new column
print(df)


# -----------------------------------------------------------
# ADD NEW ROWS
# -----------------------------------------------------------
# Create another DataFrame containing the new rows.

new_row = pd.DataFrame(
    [
        {"Name": "Arnold", "Age": 53, "Job": "BodyBuilder"},
        {"Name": "Aman", "Age": 35, "Job": "Cook"}
    ],
    index=["Emp4", "Emp5"]
)

# Combine the original DataFrame and the new rows.
# pd.concat() joins both DataFrames together.

df = pd.concat([df, new_row])

# Display the updated DataFrame
print(df)


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ DataFrame is a 2-dimensional table with rows and columns.
#
# ✔ loc[] is used to access rows using the row label (index).
#
# ✔ iloc[] is used to access rows using their integer position.
#
# ✔ A new column can be added using:
#    df["ColumnName"] = values
#
# ✔ New rows can be added by:
#    1. Creating another DataFrame
#    2. Using pd.concat() to merge both DataFrames
#
# These are some of the most commonly used DataFrame operations
# in pandas and are frequently asked in practical exams.
# ===========================================================
