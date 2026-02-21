import matplotlib.pyplot as plt
import random


plt.ion()

labels = ['A', 'B', 'C', 'D']

for i in range(10):   
    
    
    sizes = [random.randint(10, 50) for _ in labels]

    plt.clf()  
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.title("Dynamic Pie Chart")

    plt.pause(0.5)  

plt.ioff()
plt.show()