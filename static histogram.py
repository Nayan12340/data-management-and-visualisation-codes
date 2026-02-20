import matplotlib.pyplot as plt


data = [10, 20, 20, 30, 30, 30, 40, 50, 50, 60]


plt.hist(data, bins=5)


plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Static Histogram")


plt.grid(True)


plt.show()