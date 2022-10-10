import numpy as np
import pandas as pd


df = pd.read_csv('titanic.csv')
# print(df.columns)
# print(df.head())
# print(df.tail())
# df.info()
# print(df.describe())

print(df.isna().sum)