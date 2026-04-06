import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

fig, axs = plt.subplots(1, 2)
axs[0].plot(x, y1); axs[0].set_title("Chart 1")
axs[1].plot(x, y2); axs[1].set_title("Chart 2")

plt.tight_layout()
plt.show()
