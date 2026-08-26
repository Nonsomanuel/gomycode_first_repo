import pandas as pd

df = pd.Series([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])
print(df)

Mean = df.mean()
print(Mean)

Median = df.mode()
print(Median)

Mode = df.mode()
print (Mode)

Variance = df.var(ddof=0)
print(Variance)

SD = df.std(ddof=0)
print(SD)