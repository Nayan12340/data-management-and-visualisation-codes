import matplotlib.pyplot as plt
import random

# Turn on interactive mode
plt.ion()

data = []

for i in range(10):   # number of updates
    data.append(random.randint(1, 100))

    plt.clf()  # clear previous plot
    plt.hist(data, bins=5)

    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Dynamic Histogram")

    plt.pause(0.5)  # delay for animation

plt.ioff()
plt.show()