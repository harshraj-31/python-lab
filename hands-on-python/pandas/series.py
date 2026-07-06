import pandas as pd

#series = A Pandas 1-Dimensional labeled array that can hold any data type
#         Think of it like a single column in a spreadsheet (1-Dimensional)


data = [100,102,104, 200, 202]


series = pd.Series(data) #,index=["a","b","c", "d", "e"]) #can set any index

# print(series)

#TO get the Value at "a" index
# print(series.loc["a"])


#TO get the Value at "b" index
# print(series.loc["b"])


#to change the value at index["c"]
# series.loc["c"] = 74 




# get the Integer Location in short by (normal index start)
#print(series.iloc[0]) 


                                #Filtering
                                
#print(series[series >= 200])
      
# print(series[series < 200])



            #use of dictionary
calories = {"Day 1":1750, "Day 2":2000, "Day 3":1700}

series2 = pd.Series(calories)
print(series2.iloc[1])
# print(series2.loc["Day 1"])
# print(series2.loc["Day 2"])

# series2.loc["Day 3"] += 500

# print(series2.loc["Day 3"])

#                         #Filtering
# print(series2[series2 >= 2000])
# print(series2[series2 < 2000])