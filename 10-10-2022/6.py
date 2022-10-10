from matplotlib import pyplot as plt
import pandas as pd


df = pd.read_csv('Salary_Data.csv')

x_values = df['YearsExperience']
y_values = df['Salary']

plt.plot(x_values, y_values)
plt.scatter(x_values, y_values)

plt.title('T')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.legend()

plt.show()