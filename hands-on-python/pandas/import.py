import pandas as pd

# importing files

# df = pd.read_csv("pokemon.csv")
#print(df) # if the data is large then it will print first and last 5 rows

#.to_string() will print all the data no matter how big
# print(df.to_string())


df = pd.read_csv("Products.csv")
# df = pd.read_excel("Student.xlsx")
print(df)