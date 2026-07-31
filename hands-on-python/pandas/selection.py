import pandas as pd   # Import pandas library for working with datasets

# ===========================================================
#               LOAD CSV FILE
# ===========================================================
# Read the pokemon.csv file and store it in a DataFrame.
#
# index_col="Name" makes the "Name" column the row index.
# This allows us to access rows directly using Pokémon names.

df = pd.read_csv("pokemon.csv", index_col="Name")


# ===========================================================
#               SELECTING DATA IN PANDAS
# ===========================================================
# Data can be selected in two ways:
#
# 1. By Columns
# 2. By Rows
# ===========================================================


# -----------------------------------------------------------
#               SELECT A SINGLE COLUMN
# -----------------------------------------------------------
# Use the column name inside square brackets.
# The result is returned as a Series.

# print(df["Height"])
# Displays the Height column.

# print(df["Weight"])
# Displays the Weight column.

# Note:
# Since "Name" is now the index, it is no longer a normal column.
# To display it again, use:
# print(df.reset_index()["Name"])


# -----------------------------------------------------------
#             SELECT MULTIPLE COLUMNS
# -----------------------------------------------------------
# Pass a list of column names inside double square brackets.

# print(
#     df[
#         ["Height", "Weight"]
#     ].to_string()
# )

# to_string() displays the complete DataFrame
# without truncating rows.


# ===========================================================
#               SELECTING ROWS
# ===========================================================

# -----------------------------------------------------------
# USING iloc[]
# -----------------------------------------------------------
# iloc[] selects rows using their integer position.
# Index starts from 0.

# print(df.iloc[0])
# Displays the first row.

# print(df.iloc[2])
# Displays the third row.


# -----------------------------------------------------------
# USING loc[]
# -----------------------------------------------------------
# loc[] selects rows using the index label.
# Since "Name" is the index, we can search
# directly using Pokémon names.

# print(df.loc["Charizard"])
# Displays all information about Charizard.


# -----------------------------------------------------------
# SELECT SPECIFIC COLUMNS FROM A SPECIFIC ROW
# -----------------------------------------------------------
# Syntax:
# df.loc["RowLabel", ["Column1", "Column2"]]

# print(df.loc["Pikachu", ["Height", "Weight"]])
# Displays only Height and Weight of Pikachu.


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ index_col="Name"
#    Makes the Name column the DataFrame index.
#
# ✔ Single Column:
#    df["Height"]
#
# ✔ Multiple Columns:
#    df[["Height", "Weight"]]
#
# ✔ iloc[]
#    Selects rows using integer position.
#
# ✔ loc[]
#    Selects rows using index labels.
#
# ✔ Specific row and columns:
#    df.loc["Pikachu", ["Height", "Weight"]]
#
# ✔ to_string()
#    Prints the complete DataFrame without cutting rows.
# ===========================================================
