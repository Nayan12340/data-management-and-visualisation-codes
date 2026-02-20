import matplotlib.pyplot as plt
import random
import time


plt.ion()

x = []
y = []

for i in range(10):   
    x.append(i)
    y.append(random.randint(1, 50))

    plt.clf()  
    plt.plot(x, y, marker='o')

    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Dynamic Line Chart")

    plt.pause(0.5)  

plt.ioff()
plt.show()