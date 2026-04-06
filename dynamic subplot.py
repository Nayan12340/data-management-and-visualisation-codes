import matplotlib.pyplot as plt
import random
import time

fig, ax = plt.subplots()
ax.set_title("Dynamic Line Plot")
ax.set_xlim(0, 10)
ax.set_ylim(0, 50)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

x_data = []
y_data = []

for i in range(10):  # removed stray 's' here
    x_data.append(i)
    y_data.append(random.randint(0, 50))
    
    ax.clear()
    ax.plot(x_data, y_data, color='blue')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 50)
    ax.set_title("Dynamic Line Plot")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    
    plt.pause(1)

plt.show()

