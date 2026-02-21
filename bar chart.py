import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

# Create bar chart
plt.bar(categories, values)

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")

# Show graph
plt.show()