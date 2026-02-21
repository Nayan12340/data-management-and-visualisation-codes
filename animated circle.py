import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig, ax = plt.subplots()


ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)


circle, = ax.plot([], [], 'b-')


def init():
    circle.set_data([], [])
    return circle,


def update(frame):
    theta = np.linspace(0, 2*np.pi, 100)
    r = 1 + 0.5 * np.sin(frame)   

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    circle.set_data(x, y)
    return circle,


ani = animation.FuncAnimation(fig, update, frames=100,
                              init_func=init, interval=100)


plt.title("Animated Circle")
plt.show()