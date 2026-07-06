import matplotlib.pyplot as plt


# Pie Chart = Circular chart divided into slices to show percentages of the total
#               good for visualising distribution among categories

categories = ["Freshmen","Sophomores","Juiors","Seniors"]

values = [300,250,274,221]

colors = ["red","yellow","darkblue","green"]


plt.pie(values, 
        labels=categories,
        autopct="%1.1f%%",
        colors=colors,
        explode=[0,0.1,0,0.1]) #auto(autopercentage)


plt.show()