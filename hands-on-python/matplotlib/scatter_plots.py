import matplotlib.pyplot as plt

# scatter graphs = shows the relationships between two variables 
#                  helps  to identify a coorelation (+, -, None)
#                 Example : Study hours vs. Test scores              


#hours studied
x1 = [0,1,1,2,4,5,6,7,8]

#grades
y1 = [55,60,65,62,70,75,78,85,87]


#another example combine
# x2 = [0,1,1,2,4,8,6,7,8]
# y2 = [50,65,87,42,88,76,74,87,77]


plt.scatter(x1, y1,
            color="red",
            s=200,
            alpha=0.5,
            label="Class A " ) #s = size, alpha = opacity


# plt.scatter(x2, y2,
#             color="skyblue",
#             s=200,
#             alpha=0.8,
#             label="Class B " )#s = size, alpha = opacity


#labels
plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend() #TO show the labels
plt.show()