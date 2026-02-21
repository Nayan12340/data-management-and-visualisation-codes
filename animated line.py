import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


x_data = []
y_data = []


fig, ax = plt.subplots()


def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(1, 100))

    ax.clear()
    ax.plot(x_data, y_data, marker='o')
    ax.set_title("Animated Line Chart")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")


ani = animation.FuncAnimation(fig, update, frames=range(10), interval=500)


plt.show()