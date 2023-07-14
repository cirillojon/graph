import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel("data.xlsx", header=None)

# Assign columns to the loaded data
df.columns = ["Year", "My Happiness"]

# Plotting
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["My Happiness"], marker='o')

# Get the y position between 2019 and 2020
y_2019 = df.loc[df['Year'] == 2019, 'My Happiness'].values[0]
y_2020 = df.loc[df['Year'] == 2020, 'My Happiness'].values[0]
y_pos = (y_2019 + y_2020) / 2

# Add annotation
plt.annotate('Enter Erin \u2764️',
             xy=(2019, y_pos), xycoords='data',
             xytext=(50, -50), textcoords='offset points',
             arrowprops=dict(arrowstyle='->', lw=1.5),
             fontsize=12, color='red', ha='center')

plt.title('My Happiness Over Time')
plt.xlabel('Year')
plt.ylabel('My Happiness')
plt.grid(True)

plt.show()
