import pandas as pd   # Import pandas library for working with datasets

# ===========================================================
#               LOAD CSV FILE
# ===========================================================
# Read the pokemon.csv file and store it in a DataFrame.
# A DataFrame is a table with rows and columns, similar to Excel.

df = pd.read_csv("pokemon.csv")


# ===========================================================
#                     FILTERING DATA
# ===========================================================
# Filtering means selecting only those rows
# that satisfy a given condition.
#
# Syntax:
# df[condition]
#
# The rows where the condition is True are returned.
# ===========================================================


# -----------------------------------------------------------
# FIND TALL POKÉMON
# -----------------------------------------------------------
# Select Pokémon whose height is greater than or equal to 2.

# tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)


# -----------------------------------------------------------
# FIND HEAVY POKÉMON
# -----------------------------------------------------------
# Select Pokémon whose weight is greater than 100.

# heavy_pokemon = df[df["Weight"] > 100]
# print(heavy_pokemon)


# -----------------------------------------------------------
# FIND LEGENDARY POKÉMON
# -----------------------------------------------------------
# Legendary column contains:
# 1 -> Legendary Pokémon
# 0 -> Normal Pokémon

# legendary_pokemon = df[df["Legendary"] == 1]
# print(legendary_pokemon)


# -----------------------------------------------------------
# FIND WATER TYPE POKÉMON
# -----------------------------------------------------------
# Option 1:
# Select Pokémon whose primary type is Water.

# water_pokemon = df[df["Type1"] == "Water"]

# Option 2:
# Select Pokémon where either Type1 OR Type2 is Water.
# The OR operator (|) returns rows if at least one condition is True.

# water_pokemon = df[
#     (df["Type1"] == "Water") |
#     (df["Type2"] == "Water")
# ]

# print(water_pokemon)


# -----------------------------------------------------------
# FIND FIRE + FLYING TYPE POKÉMON
# -----------------------------------------------------------
# The AND operator (&) returns rows only when
# both conditions are True.

# ff_pokemon = df[
#     (df["Type1"] == "Fire") &
#     (df["Type2"] == "Flying")
# ]

# print(ff_pokemon)


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ Filtering is used to select rows based on a condition.
#
# ✔ Comparison Operators:
#    ==  Equal to
#    !=  Not equal to
#    >   Greater than
#    <   Less than
#    >=  Greater than or equal to
#    <=  Less than or equal to
#
# ✔ Logical Operators:
#    &  -> AND (Both conditions must be True)
#    |  -> OR  (At least one condition must be True)
#
# ✔ General Syntax:
#    df[condition]
#
# ✔ Example:
#    df[df["Height"] >= 2]
#    Returns all Pokémon with height 2 or more.
# ===========================================================
