import matplotlib.pyplot as plt
import random


plt.ion()

x = []
y1 = []
y2 = []

for i in range(10):   
    
    x.append(i)
    y1.append(random.randint(10, 50))
    y2.append(random.randint(5, 40))

    plt.clf()  

    
    plt.subplot(1, 2, 1)
    plt.plot(x, y1, marker='o')
    plt.title("Dynamic Line")

    
    plt.subplot(1, 2, 2)
    plt.bar(x, y2)
    plt.title("Dynamic Bar")

    plt.tight_layout()
    plt.pause(0.5) 

plt.ioff()
plt.show()