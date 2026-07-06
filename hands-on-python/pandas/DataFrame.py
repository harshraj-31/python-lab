import pandas as pd

#DataFrame = A tabular data structude with rows and columns . (2 Dimensional)
#               SIMILAR TO EXCEL SPREADSHEET


data = {"Name": ["Karan","Anas","Harry"],
       "Age": [22, 21, 20]
    }

df = pd.DataFrame(data, index=["Emp1","Emp2","Emp3"])

# print(df)

#Search using loc/
# print(df.loc["Emp3"])
# print(df.loc["Emp2"])


# search using integerLocation (index)
# print(df.iloc[0])
# print(df.iloc[1])


#Add a new Column
df["Job"] = ["CEO","N/A","cashier"]

print(df)


# #Add a new ROW
new_row = pd.DataFrame(
    [
    {"Name": "Arnold", "Age":53,"Job":"BodyBuilder"},
    {"Name":"Aman", "Age":35, "Job":"Cook"} 
    ],
    index=["emp4", "emp5"]
    )

df = pd.concat([df, new_row])
print(df)

