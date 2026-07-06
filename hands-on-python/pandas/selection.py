import pandas as pd

#index_col="Name" will help set index as name
df = pd.read_csv("pokemon.csv",index_col="Name") 

#                   SELECTION BY COLUMN

#         >  to print SINGLE  columns

# print(df["Name"]) #use to_string to print all name
# print(df["Height"])
# print(df["Weight"])



#       > to print multiple columns

# print(df[
#     ["Name","Height","Weight"]
#     ].to_string())




#                   SELECTION BY ROWS


# print(df.iloc[0])
# print(df.loc["Charizard"])

# print(df.loc["Pikachu", ["Height", "Weight"]]) 

# print(df.iloc[0])