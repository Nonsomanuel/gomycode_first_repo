import pandas as pd

df =pd.Series([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])
print(df)
#find the mean of the data
Mean =df.mean()
print(f'mean: {Mean:,.2f}')

Median =df.median()
print(f'median: {Median:,.2f}')

Mode =df.mode()
print(f'mode: {Mode}')

Variance =df.var(ddof=0)
print(f'variance: {Variance:,.2f}')

std=df.std()
print(f'standard deviation: {std:,.2f}')