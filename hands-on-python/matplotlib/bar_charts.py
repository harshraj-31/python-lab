import matplotlib.pyplot as plt

# bar chart = compare categories of data by
# representing each category with a bar

categories = ["Grains","Fruit","vegetables","Protien","Dairy","Sweets"]

values = [4,3,5,5,4,1]


plt.bar(categories,values,color="red")
#for horizontal bar chart use 
# plt.barh(categories,values,color="skyblue")

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantiy")



plt.show()