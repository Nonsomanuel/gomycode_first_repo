import pandas as pd

df = pd.Series([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])
print(df)

mean = df.mean()
print(f'mean:{mean:,.2f}')

median = df.median()
print(f'median:{median:,.2f}')

mode = df.mode()
print(mode)

variance = df.var(ddof=0)
print(f'variance{variance:,.2f}')

Standard_deviation = df.std(ddof=0)
print(f'standard deviation{Standard_deviation:,.2f}')


