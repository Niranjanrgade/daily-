import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Salary_Data.csv')
plt.plot(df['YearsExperience'], df['Salary'])
plt.legend()
plt.show()