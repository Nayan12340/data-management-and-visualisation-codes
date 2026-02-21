import matplotlib.pyplot as plt
import random


plt.ion()

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

for i in range(10):   
    
    
    values = [random.randint(5, 30) for _ in categories]

    plt.clf()  
    plt.bar(categories, values)

    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Dynamic Bar Chart")

    plt.pause(0.5)  
    

plt.ioff()
plt.show()