

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import plotly.express as px

 


df = pd.read_csv("dataset_100.csv")

 

# Check columns (IMPORTANT)

print("Columns:", df.columns)

 


# 🥧 1. Pie Chart (Company-wise count)



company_counts = df['Company'].value_counts()

 

plt.figure(figsize=(6,6))

plt.pie(company_counts, labels=company_counts.index, autopct='%1.1f%%')

plt.title("Employees per Company")

plt.show()


# 🔻 2. Funnel Chart (Railway-wise)


railway_counts = df['Railway'].value_counts().reset_index()

railway_counts.columns = ['Railway', 'Count']

 

fig = px.funnel(railway_counts, x='Count', y='Railway', title="Railway-wise Funnel Chart")

fig.show()

 



# 📊 3. Bar Chart (Company vs Year)


bar_data = df.groupby(['Company', 'Year']).size().unstack()

 

bar_data.plot(kind='bar', figsize=(10,6))

plt.title("Company vs Year")

plt.ylabel("Count")

plt.xlabel("Company")

plt.xticks(rotation=45)

plt.show()

 


# 📈 4. Line Chart (Company vs C_Type)


line_data = df.groupby(['Company', 'C_Type']).size().unstack()

 

line_data.T.plot(figsize=(10,6))

plt.title("Company vs C_Type")

plt.ylabel("Count")

plt.xlabel("C_Type")

plt.show()

 

# 📉 5. Histogram (Review Count)


plt.figure(figsize=(8,5))

sns.histplot(df['Review_Count'], bins=10)

plt.title("Review Count Distribution")

plt.xlabel("Review Count")

plt.ylabel("Frequency")

plt.show()