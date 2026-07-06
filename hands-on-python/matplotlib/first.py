

import matplotlib.pyplot as plt

#normal plot customization

x =  [2023,2024,2025,2026]

y = [15,25,30,20]




plt.plot(x,y, marker=".",
        markersize=20,
        markerfacecolor="red",
        linestyle="dotted")


plt.grid() #helps to make plots easier to read 

plt.title("Class Size", fontsize="15",color="red")

plt.xlabel("Year",fontsize=10,color="darkblue")

plt.ylabel("Students", fontsize=10,color="darkblue")

plt.show()


