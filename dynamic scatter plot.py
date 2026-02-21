import matplotlib.pyplot as plt
import random


plt.ion()

x = []
y = []

for i in range(10):   
    
    
    x.append(random.randint(1, 50))
    y.append(random.randint(1, 50))

    plt.clf()  
    plt.scatter(x, y)

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Dynamic Scatter Plot")

    plt.pause(0.5) 

plt.ioff()
plt.show()