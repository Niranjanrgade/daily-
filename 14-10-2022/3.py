import pandas as pd

models = ["i20", "i10", "sonet", "seltos", "meridian", "compass", "X7", "x3"]
companies = ["hyundai", "hyundai", "kia", "kia", "jeep", "jeep", "bmw", "bmw"]

s = pd.Series(models)
print(s)
s2 = pd.Series(companies)
print(s2)

s3 = pd.Series(models, index=companies)
print(s3)

print(s3['jeep'])