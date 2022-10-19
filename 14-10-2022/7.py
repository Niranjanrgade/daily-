import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('50_Startups.csv')
del df['State']
x = list(df.columns)
print(x)
y = list(df.sum())
print(y)
y2 = list(df.sum() + 20000)
print(y2)

plt.subplot(1,2,1)
plt.barh(x, y)
plt.subplot(1,2,2)
plt.bar(x, y2)
plt.show()