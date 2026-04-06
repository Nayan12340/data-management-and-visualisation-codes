import matplotlib.pyplot as plt
import random
import time

x_values = []
y_values = []

plt.ion()

for i in range(10):
    x_values.append(i)
    y_values.append(random.randint(1, 10))

    plt.clf()  
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Dynamic Line Graph (Not Animated)")
    plt.pause(0.5)  

plt.ioff()
plt.show()
